from typing import Type, Callable, List, Literal

import numpy as np
import pandas as pd
from spacy.tokens import Doc
from sklearn.base import BaseEstimator
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.feature_extractor import FeatureExtractor

SCORERS_TO_REPORT: List[Callable[[np.ndarray, np.ndarray], float]] = [
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
]


class Experiment:
    def __init__(
        self,
        docs: "pd.Series[Doc]",
        labels: "pd.Series[str]",
        train_test_dev: "pd.Series[Literal['train', 'test', 'dev']]",
        spacy_model_name: str,
        feature_extractors: List[FeatureExtractor],
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

    def run(self) -> None:
        """Runs the experiment."""
        pass  # FIXME: Implement this method

    def report_results(self) -> pd.DataFrame:
        """Returns a DataFrame containing the results of the experiment."""
        pass  # FIXME: Implement this method
