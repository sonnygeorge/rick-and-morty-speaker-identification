from functools import partial
from typing import List, Type

from sklearn.base import BaseEstimator

from src.schema.experiment import Experiment


class ConfiguredExperiment(Experiment):
    """A dataclass for storing the configuration of an experiment."""

    def __init__(
        self,
        feature_extractor_names: List[str],
        spacy_model_name: str,
        model_type: Type[BaseEstimator],
        use_by_episode_splits: bool = False,
        **kwargs
    ):
        self.feature_extractor_names = feature_extractor_names
        self.spacy_model_name = spacy_model_name
        self.use_by_episode_splits = use_by_episode_splits
        self.ExperimentType = partial(Experiment, model_type=model_type, **kwargs)
