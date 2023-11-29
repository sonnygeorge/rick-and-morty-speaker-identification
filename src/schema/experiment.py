from typing import Type, Literal, Dict, Optional, Tuple
from time import perf_counter
import os

import numpy as np
import pandas as pd
from spacy.tokens import Doc
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer

from src.schema.feature_extractor import FeatureExtractor
from src.globals import SCORERS, RESULTS_CSV_FPATH

# TODO:
#   - Experiment names
#   - Sum feature importance across extractors
#   - Re-train after omitting features with 0 importance?


class Experiment:
    def __init__(
        self,
        docs: "pd.Series[Doc]",
        labels: "pd.Series[str]",
        train_test_dev: "pd.Series[Literal['train', 'test', 'dev']]",
        feature_extractors: Dict[str, FeatureExtractor],
        spacy_model_name: str,  # Taken and stored for report
        spacy_model_load_time: float,  # Taken and stored for report
        avg_utterance_preprocessing_time: float,  # Taken and stored for report
        model_type: Type[BaseEstimator],
        name: Optional[str] = None,
        **model_kwargs,
    ):
        self.docs = docs
        self.labels = labels
        self.train_test_dev = train_test_dev
        self.spacy_model_name = spacy_model_name
        self.feature_extractors = feature_extractors
        self.spacy_model_load_time = spacy_model_load_time
        self.avg_utterance_preprocessing_time = avg_utterance_preprocessing_time
        self.avg_feature_extraction_time = None
        self.model_type = model_type
        self.model = model_type(**model_kwargs)
        self.features: pd.DataFrame = None
        self.train_scores: Dict[str, float] = {}
        self.dev_scores: Dict[str, float] = {}
        self.test_scores: Dict[str, float] = {}
        self.importances: Optional[pd.Series] = None
        if name is None:
            name = self._generate_name()
        self.name = name

    def _generate_name(self) -> str:
        """Generates a name for the experiment from its model & feature extractors."""

        def is_other(s):
            return not ("bedd" in s or "gram" in s or "topi" in s or "propor" in s)

        all_features_str = "_".join(self.feature_extractors.keys()).lower()
        name = f"{self.model_type.__name__}_{len(self.feature_extractors)}fes_("
        if "gram" in all_features_str:
            name += "ngrams+"
        if "embedding" in all_features_str:
            name += "vecs+"
        if all_features_str.count("proportion") > 1:
            name += "proportions+"
        if all_features_str.count("topic") > 1:
            name += "topics+"
        if len([f for f in self.feature_extractors.keys() if not is_other(f)]) > 0:
            name += "other+"
        name = name[:-1] + ")"
        return name

    def _extract_features_from_doc(self, idx: int) -> Dict[str, float]:
        """Extracts features from a SpaCy Doc object given its idx."""
        features = {}
        doc = self.docs[idx]
        for feature_extractor in self.feature_extractors.values():
            features.update(feature_extractor(doc))
        return features

    def run(self) -> None:
        """Runs the experiment."""
        print("🚀 Extracting features...")
        # Extract features
        start = perf_counter()
        feature_dicts = self.docs.index.map(self._extract_features_from_doc)
        self.avg_feature_extraction_time = (perf_counter() - start) / len(self.docs)
        dict_vectorizer = DictVectorizer()
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
        dev_predictions = self.model.predict(dev_features)
        for name, scorer in SCORERS.items():
            self.dev_scores[name] = np.round(scorer(dev_labels, dev_predictions), 3)
        # Score model on test set
        test_features = self.features[self.train_test_dev == "test"]
        test_labels = self.labels[self.train_test_dev == "test"]
        test_predictions = self.model.predict(test_features)
        for name, scorer in SCORERS.items():
            self.test_scores[name] = np.round(scorer(test_labels, test_predictions), 3)
        # Save feature importances if available
        if hasattr(self.model, "feature_importances_"):
            self.importances = pd.Series(
                self.model.feature_importances_, index=self.features.columns
            ).sort_values(ascending=False)

    def print_results(self) -> None:
        print("\n================================================================")
        print(f"{self.name} Results")
        print("================================================================")
        print("🤖 Model Type:\n\t", self.model_type)
        if hasattr(self.model, "class_prior_"):
            print(self.model.classes_)
            print(self.model.class_prior_)
        print("  - Number of Features:\n\t", len(self.features.columns))
        if self.importances is not None:
            print(f"🧠 Most Important Features:\n\t{self.importances[:10]}")
            n_zero_importance = len(self.importances[self.importances == 0])
            print("  - Number of Features With 0 Importance:\n\t", n_zero_importance)
        print("🧠 Feature Varieties:\n\t", list(self.feature_extractors.keys()))
        print("📊 Train Scores:\n\t", self.train_scores)
        print("📊 Dev Scores:\n\t", self.dev_scores)
        print("📊 Test Scores:\n\t", self.test_scores)
        print("⌛ Times (s):")
        print(f"\tAvg. SpaCy Processing: {self.avg_utterance_preprocessing_time:.3f}")
        print(f"\tAvg. Feature Extraction: {self.avg_feature_extraction_time:.4f}")
        print(f"\tModel Training: {self.model_train_time:.3f}")
        print(f"\tSpaCy Model Load: {self.spacy_model_load_time:.3f}")
        print("================================================================")
        print("================================================================\n")

    def save_markdown_report(self) -> None:
        pass

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
