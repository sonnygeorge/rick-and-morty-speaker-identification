from typing import Type, Literal, Dict, Optional, Tuple, Set
from time import perf_counter
from collections import defaultdict
import os
import re

import numpy as np
import pandas as pd
from spacy.tokens import Doc
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

from src.schema.feature_extractor import FeatureExtractor
from src.globals import SCORERS, RESULTS_CSV_FPATH, DATA_DIR_PATH


class Experiment:
    def __init__(
        self,
        docs: "pd.Series[Doc]",
        labels: "pd.Series[str]",
        train_test_dev: "pd.Series[Literal['train', 'test', 'dev']]",
        previous_speakers: "pd.Series[str]",
        feature_extractors: Dict[str, Optional[FeatureExtractor]],
        spacy_model_name: str,  # Taken and stored for report
        use_by_episode_splits: bool,
        model_type: Type[BaseEstimator],
        name: Optional[str] = None,
        **model_kwargs,
    ):
        self.docs = docs
        self.label_encoder = LabelEncoder()
        self.labels = pd.Series(self.label_encoder.fit_transform(labels))
        self.train_test_dev = train_test_dev
        self.previous_speakers = previous_speakers
        self.spacy_model_name = spacy_model_name
        self.feature_extractors = feature_extractors
        self.use_by_episode_splits = use_by_episode_splits
        self.avg_feature_extraction_time = None
        self.model_type = model_type
        self.model = model_type(**model_kwargs)
        self.features: pd.DataFrame = None
        self.train_scores: Dict[str, float] = {}
        self.dev_scores: Dict[str, float] = {}
        self.test_scores: Dict[str, float] = {}
        self.importances: Optional[pd.Series] = None
        self.coefs: Optional[pd.Series] = None
        self.dev_classification_report: Optional[dict] = None
        self.test_classification_report: Optional[dict] = None
        self.incorrect_texts: Optional[pd.Series] = None
        self.incorrect_preds: Optional[pd.Series] = None
        self.incorrect_labels: Optional[pd.Series] = None
        self.feature_names_by_extractor: Dict[str, Set[str]] = defaultdict(set)
        self.model_params = model_kwargs
        if name is None:
            name = self._generate_base_name()
        self.name = name

    def _generate_base_name(self) -> str:
        """Generates a base name for the experiment from its model & feature extractors."""
        model_str = re.sub(r"[aeiou]", "", self.model_type.__name__)
        return f"{model_str}_{len(self.feature_extractors)}fs"

    def _extract_features_from_doc(self, idx: int) -> Dict[str, float]:
        """Extracts features for an index of `self.docs`."""
        features = {}
        doc = self.docs[idx]
        for extractor_name, feature_extractor in self.feature_extractors.items():
            if extractor_name == "Previous Speaker":
                prev_speaker = self.previous_speakers[idx]
                # if prev_speaker not in SANCHEZ_FAMILY_LABELS:  # (This makes it worse)
                #     if pd.isna(prev_speaker):
                #         prev_speaker = "None"
                #     else:
                #         prev_speaker = "Other"
                extracted = {f"prev_speaker({prev_speaker})": 1}
            else:
                extracted = feature_extractor(doc)
            features.update(extracted)
            self.feature_names_by_extractor[extractor_name].update(
                set(extracted.keys())
            )
        return features

    def run(self) -> None:
        print("🚀 Extracting features...")
        # Extract features
        start = perf_counter()
        feature_dicts = self.docs.index.map(self._extract_features_from_doc)
        self.avg_feature_extraction_time = (perf_counter() - start) / len(self.docs)
        dict_vectorizer = (
            DictVectorizer()
        )  # FIXME: Fit transform on train only / transform others?
        self.features = pd.DataFrame(
            dict_vectorizer.fit_transform(feature_dicts).toarray(),
            index=self.docs.index,
            columns=dict_vectorizer.feature_names_,
        )
        # Train model
        train_features = self.features[self.train_test_dev == "train"]
        train_labels = self.labels[self.train_test_dev == "train"]
        start = perf_counter()
        print("🚀 Beginning training...")
        self.model.fit(X=train_features, y=train_labels)
        self.model_train_time = perf_counter() - start
        # Score model on train set
        train_predictions = self.model.predict(train_features)
        for name, scorer in SCORERS.items():
            self.train_scores[name] = np.round(
                scorer(train_labels, train_predictions), 3
            )
        # Score model on dev set
        dev_features = self.features[self.train_test_dev == "dev"]
        dev_labels = self.labels[self.train_test_dev == "dev"]
        dev_predictions = pd.Series(
            self.model.predict(dev_features), index=dev_labels.index
        )
        for name, scorer in SCORERS.items():
            self.dev_scores[name] = np.round(scorer(dev_labels, dev_predictions), 3)
        # Save incorrect predictions
        dev_docs = self.docs[self.train_test_dev == "dev"]
        incorrect_docs = dev_docs[dev_predictions != dev_labels]
        self.incorrect_texts = incorrect_docs.map(lambda doc: doc.text)
        self.incorrect_preds = dev_predictions[dev_predictions != dev_labels]
        self.incorrect_labels = dev_labels[dev_predictions != dev_labels]
        # Score model on test set
        test_features = self.features[self.train_test_dev == "test"]
        test_labels = self.labels[self.train_test_dev == "test"]
        test_predictions = self.model.predict(test_features)
        for name, scorer in SCORERS.items():
            self.test_scores[name] = np.round(scorer(test_labels, test_predictions), 3)
        # Save feature importances if available
        if hasattr(self.model, "feature_importances_"):
            if len(self.model.feature_importances_.shape) > 1:
                importances = np.mean(self.model.feature_importances_, axis=1)
            else:
                importances = self.model.feature_importances_
            self.importances = pd.Series(
                importances, index=self.features.columns
            ).sort_values(ascending=False)
        # Save coefficients if available
        if hasattr(self.model, "coef_"):
            self.coefs = pd.Series(self.model.coef_[0], index=self.features.columns)
        # Save classification reports
        self.dev_classification_report = classification_report(
            dev_labels, dev_predictions, output_dict=True
        )
        self.test_classification_report = classification_report(
            test_labels, test_predictions, output_dict=True
        )

    def print_results(self) -> None:
        print(f"\n=== {self.name} Results ===\n")
        print("  - Model Type:\n\t", self.model_type)
        print("  - Model Hyperparameters:\n\t", self.model_params)
        print("  - Number of Features:\n\t", len(self.features.columns))
        print("  - Feature Varieties:")
        for extractor_name in self.feature_extractors.keys():
            print(f"\t- {extractor_name}")
        print("  - Scores:")
        print("\t- Train:")
        for metric, score in self.train_scores.items():
            print(f"\t\t- {metric}: {score}")
        print("\t- Dev:")
        for metric, score in self.dev_scores.items():
            print(f"\t\t- {metric}: {score}")
        print("\t- Test:")
        for metric, score in self.test_scores.items():
            print(f"\t\t- {metric}: {score}")
        print("  - Times (s):")
        print(f"\tAvg. Feature Extraction: {self.avg_feature_extraction_time:.4f}")
        print(f"\tModel Training: {self.model_train_time:.3f}")

    def save_markdown_report(self) -> None:
        md = f"### 🚀 **{self.name}**\n\n"
        md += f"- 🤖 **Model Type**: \n\t{self.model_type}\n"
        dataset_used = "By Episode" if self.use_by_episode_splits else "Random"
        md += f"- 📊 **Dataset Used**: \n\t_{dataset_used}_\n"
        md += f"- 🧠 **Number of Features**: \n\t{len(self.features.columns)}\n"
        if self.coefs is not None:
            n_unused = len(self.coefs[self.coefs == 0])
            md += f"- 🚫 **Unused Features**: \n\t{n_unused}/{len(self.coefs)}\n"
        elif self.importances is not None:
            n_unused = len(self.importances[self.importances == 0])
            md += f"- 🚫 **Unused Features**: \n\t{n_unused}/{len(self.importances)}\n"
        md += f"- ⌛ **Model Train Time**: \n\t{self.model_train_time:.3f}\n"
        md += f"- 💬 **SpaCy Preprocessing Model**: \n\t`{self.spacy_model_name}`\n\n"
        if self.model_params:
            md += f"- 🧬 **Model Hyperparameters**:\n\n"
            for param, value in self.model_params.items():
                md += f"\t- `{param}`: {value}\n"
        md += "\n"
        md += "### 📊 Scores\n\n"
        md += f"| Metric | Train | Dev | Test |\n"
        md += f"| ------ | ----- | --- | ---- |\n"
        for metric, train_score in self.train_scores.items():
            md += f"| {metric} | {train_score} | {self.dev_scores[metric]} | "
            md += f"{self.test_scores[metric]} |\n"
        md += "\n"
        md += "#### Classification Report (Dev Set)\n\n"
        md += "| Label | Precision | Recall | F1-Score |\n"
        md += "| ----- | --------- | ------ | -------- |\n"
        for label, report in self.dev_classification_report.items():
            if label == "accuracy" or "avg" in label:
                continue
            decoded_lbl = self.label_encoder.inverse_transform([int(label)])[0]
            md += f"| {decoded_lbl} | {report['precision']:.2f} | {report['recall']:.2f} | "
            md += f"{report['f1-score']:.2f} |\n"
        md += "\n#### Classification Report (Test Set)\n\n"
        md += "| Label | Precision | Recall | F1-Score |\n"
        md += "| ----- | --------- | ------ | -------- |\n"
        for label, report in self.test_classification_report.items():
            if label == "accuracy" or "avg" in label:
                continue
            decoded_lbl = self.label_encoder.inverse_transform([int(label)])[0]
            md += f"| {decoded_lbl} | {report['precision']:.2f} | {report['recall']:.2f} | "
            md += f"{report['f1-score']:.2f} |\n"
        if len(self.feature_extractors) >= 1:
            md += "\n### 🧠 Feature Extraction Methods\n\n"
            if self.importances is not None:
                md += "| Method | Importance |\n"
                md += "| ------ | ---------- |\n"
            else:
                md += "| Method |\n"
                md += "| ------ |\n"
            if self.importances is None:
                for extractor_name in self.feature_extractors.keys():
                    md += f"| {extractor_name} |\n"
            else:
                importances = {}
                for extractor_name in self.feature_extractors.keys():
                    importance = self.importances[
                        list(self.feature_names_by_extractor[extractor_name])
                    ].sum()
                    importances[extractor_name] = importance
                sorted_importances = sorted(
                    importances.items(), key=lambda x: x[1], reverse=True
                )
                for extractor_name, importance in sorted_importances:
                    md += f"| {extractor_name} | {importance:.4f} |\n"
        md += "\n### 🚫 Incorrect Predictions\n\n"
        md += "| Utterance | Predicted Speaker | Actual Speaker |\n"
        md += "| --------- | ----------------- | -------------- |\n"
        for text, pred, label in zip(
            self.incorrect_texts, self.incorrect_preds, self.incorrect_labels
        ):
            pred_decoded_lbl = self.label_encoder.inverse_transform([int(pred)])[0]
            true_decoded_lbl = self.label_encoder.inverse_transform([int(label)])[0]
            md += f"| {text} | {pred_decoded_lbl} | {true_decoded_lbl} |\n"
        if self.importances is not None:
            md += "### 📉 Individual Feature Importances\n\n"
            md += "| Feature | Importance |\n"
            md += "| ------- | ---------- |\n"
            importances = list(self.importances.items())
            for feature, importance in importances[:18]:
                md += f"| {feature} | {importance} |\n"
            if len(importances) > 60:
                md += "| ... | ... |\n"
                for feature, importance in importances[-30:]:
                    md += f"| {feature} | {importance} |\n"
            else:
                for feature, importance in importances[30:]:
                    md += f"| {feature} | {importance} |\n"
        if self.coefs is not None:
            unused_coefs = self.coefs[self.coefs == 0]
            if len(unused_coefs) > 0:
                md += "### 📉 Unused Features\n\n"
                md += f"{len(unused_coefs)}/{len(self.coefs)} features were unused.\n\n"
                md += "| Feature | Coefficient |\n"
                md += "| ------- | ----------- |\n"
                unused_coefs = list(unused_coefs.items())
                for feature, coef in unused_coefs[:18]:
                    md += f"| {feature} | {coef} |\n"
                if len(unused_coefs) > 36:
                    md += "| ... | ... |\n"
                    for feature, coef in unused_coefs[-18:]:
                        md += f"| {feature} | {coef} |\n"
                else:
                    for feature, coef in unused_coefs[18:]:
                        md += f"| {feature} | {coef} |\n"
        with open(os.path.join(DATA_DIR_PATH, f"{self.name}.md"), "w") as f:
            f.write(md)

    def add_row_to_results_csv(self) -> None:
        if os.path.exists(RESULTS_CSV_FPATH):
            df = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)
            # Update base name if it already exists
            shared_base_name_df = df[df.index.str.startswith(self.name)]
            if len(shared_base_name_df) > 0:
                self.name += f"_{len(shared_base_name_df) + 1}"
            else:
                self.name += "_1"
            df.loc[self.name] = self.dev_scores  # Add row to df
        else:
            # Add a one to the name
            self.name += "_1"
            df = pd.DataFrame([self.dev_scores], index=[self.name])
        df.to_csv(RESULTS_CSV_FPATH)

    def report_results(self) -> pd.DataFrame:
        self.add_row_to_results_csv()
        self.print_results()
        self.save_markdown_report()
