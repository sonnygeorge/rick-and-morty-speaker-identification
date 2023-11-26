from functools import partial
from typing import Dict, Callable

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

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

macro_f1_score = partial(f1_score, average="macro")

SCORERS: Dict[str, Callable[[np.ndarray, np.ndarray], float]] = {
    "Accuracy": accuracy_score,
    "Macro F1": macro_f1_score,
}
