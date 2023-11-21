from typing import Dict, List

from sklearn.tree import DecisionTreeClassifier

from src.feature_extractors import (
    get_avg_noun_embedding,
    get_avg_verb_embedding,
)
from src.schema.feature_extractor import FeatureExtractor
from src.schema.configured_experiment import ConfiguredExperiment
from src.globals import SEED


FEATURE_EXTRACTORS: Dict[str, FeatureExtractor] = {
    "Average Noun Embedding": get_avg_noun_embedding,
    "Average Verb Embedding": get_avg_verb_embedding,
}


CONFIGURED_EXPERIMENTS: List[ConfiguredExperiment] = [
    ConfiguredExperiment(
        feature_extractor_names=["Average Noun Embedding", "Average Verb Embedding"],
        spacy_model_name="en_core_web_sm",
        model_type=DecisionTreeClassifier,
        criterion="entropy",
        max_depth=5,
        random_state=SEED,
    ),
]
