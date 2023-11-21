from functools import partial

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from src.schema.feature_extractor import FeatureExtractor
from typing import List, Callable

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
macro_f1_score.__name__ = "macro_f1_score"

SCORERS: List[Callable[[np.ndarray, np.ndarray], float]] = [
    accuracy_score,
    macro_f1_score,
]
