from typing import Type, Literal, Dict

import pandas as pd
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
        spacy_model_name: str,
        feature_extractors: Dict[str, FeatureExtractor],
        model_load_time: float,  # Taken and stored for report
        avg_utterance_preprocessing_time: float,  # Taken and stored for report
        model_type: Type[BaseEstimator],
        **model_kwargs,
    ):
        self.docs = docs
        self.labels = labels
        self.train_test_dev = train_test_dev
        self.spacy_model_name = spacy_model_name
        self.feature_extractors = feature_extractors
        self.model_load_time = model_load_time
        self.avg_utterance_preprocessing_time = avg_utterance_preprocessing_time
        self.model = model_type(**model_kwargs)
        self.features: pd.DataFrame = None
        self.feature_vocabulary: dict = None
        self.scores: Dict[str, float] = {}

    def _extract_features_from_doc(self, doc: Doc) -> Dict[str, float]:
        features = {}
        for feature_extractor in self.feature_extractors.values():
            features.update(feature_extractor(doc))
        return features

    def run(self) -> None:
        """Runs the experiment."""
        # Extract features
        feature_dicts = self.docs.apply(self._extract_features_from_doc)
        dict_vectorizer = DictVectorizer()
        self.features = pd.DataFrame(
            dict_vectorizer.fit_transform(feature_dicts).toarray(),
            index=self.docs.index,
        )
        # Train model
        train_features = self.features[self.train_test_dev == "train"]
        train_labels = self.labels[self.train_test_dev == "train"]
        self.model.fit(X=train_features, y=train_labels)
        # Score model on dev set
        dev_features = self.features[self.train_test_dev == "dev"]
        dev_labels = self.labels[self.train_test_dev == "dev"]
        dev_predictions = self.model.predict(dev_features)
        # Report scores
        for name, scorer in SCORERS.items():
            self.scores[name] = scorer(dev_labels, dev_predictions)

    def report_results(self) -> pd.DataFrame:
        """Returns a DataFrame containing the results of the experiment."""
        print(list(self.feature_extractors.keys()))
        print(self.scores)  # FIXME
