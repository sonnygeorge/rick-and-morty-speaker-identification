from functools import partial
from typing import Dict, List

from src.experiment import Experiment


class ConfiguredExperiment(Experiment):
    """A dataclass for storing the configuration of an experiment."""

    def __init__(
        self,
        feature_extractor_names: List[str],
        spacy_model_name: str,
        model: type,
        **kwargs
    ):
        self.feature_extractor_names = feature_extractor_names
        self.spacy_model_name = spacy_model_name
        self.Experiment = partial(Experiment, model, **kwargs)
