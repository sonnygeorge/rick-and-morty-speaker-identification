from typing import Type, Literal, Dict
from time import perf_counter

import pandas as pd
import numpy as np
from spacy.tokens import Doc
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer

from src.schema.feature_extractor import FeatureExtractor
from src.globals import SCORERS


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
        self.scores: Dict[str, float] = {}

    def _extract_features_from_doc(self, idx: int) -> Dict[str, float]:
        """Extracts features from a SpaCy Doc object given its idx."""
        features = {}
        doc = self.docs[idx]
        for feature_extractor in self.feature_extractors.values():
            features.update(feature_extractor(doc))
        return features

    def run(self) -> None:
        """Runs the experiment."""
        print("🚀 Running experiment...")
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
        # Score model on dev set
        dev_features = self.features[self.train_test_dev == "dev"]
        dev_labels = self.labels[self.train_test_dev == "dev"]
        dev_predictions = self.model.predict(dev_features)
        # Report scores
        for name, scorer in SCORERS.items():
            self.scores[name] = scorer(dev_labels, dev_predictions)

    def report_results(self) -> pd.DataFrame:  # TODO: markdown file? csv?
        importances = pd.Series(
            self.model.feature_importances_, index=self.features.columns
        )
        importances = importances.sort_values(ascending=False)
        top = importances.head(13)
        top = {name: f"{score:.3f}" for name, score in top.items()}
        zero = importances[importances == 0][:13]
        print("\n================================================================")
        print("===================== 🧪 Experiment Report =====================")
        print("================================================================")
        print("🤖 Model Type:\n\t", self.model_type)
        print(f"🧠 Most Important Features:\n\t{top}")
        print("🧠 Zero Importance Features:\n\t", list(zero.index[:40]))
        print("  - Number of Features:\n\t", len(self.features.columns))
        print("  - Number of Features With 0 Importance:\n\t", len(zero))
        print("🧠 Feature Varieties:\n\t", list(self.feature_extractors.keys()))
        print("📊 Scores:\n\t", self.scores)
        print("⌛ Times (s):")
        print(f"\tAvg. SpaCy Processing: {self.avg_utterance_preprocessing_time:.3f}")
        print(f"\tAvg. Feature Extraction: {self.avg_feature_extraction_time:.4f}")
        print(f"\tModel Training: {self.model_train_time:.3f}")
        print(f"\tSpaCy Model Load: {self.spacy_model_load_time:.3f}")
        print("================================================================")
        print("================================================================\n")
