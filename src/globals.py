from functools import partial

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.schema.feature_extractor import FeatureExtractor
from typing import Dict, Callable

import numpy as np


SEED = 42
DATA_FPATH = "data.csv"
SANCHEZ_FAMILY_LABELS = {
    "Rick",
    "Morty",
    "Beth",
    "Jerry",
    "Summer",
}
SPLIT_RATIOS = {"train": 0.74, "dev": 0.13, "test": 0.13}
ENABLED_SPACY_COMPONENTS = ["tagger", "parser", "ner"]

macro_f1_score = partial(f1_score, average="macro")

SCORERS: Dict[str, Callable[[np.ndarray, np.ndarray], float]] = {
    "Accuracy": accuracy_score,
    "Macro F1": macro_f1_score,
}
