import os
from functools import partial
from typing import Dict, Callable

from sklearn.metrics import accuracy_score, f1_score
import numpy as np

from src.word_clusters import (
    DEATH_WORDS,
    DUBIETY_WORDS,
    CONDESCENSION_WORDS,
    INTOXICATION_WORDS,
    GRATITUDE_WORDS,
    SCIFI_CREATURE_WORDS,
    GENERIC_EMOTIION_WORDS,
    FANCY_SCIENCE_WORDS,
    SEXUAL_WORDS,
    FOOD_WORDS,
)


_DATA_DIR = "data"
_RAW_SCRIPT_DATA_FNAME = "RickAndMortyScripts.csv"
_TRAIN_DATA_FNAME = "train_data.csv"
_DEV_DATA_FNAME = "dev_data.csv"
_TEST_DATA_FNAME = "test_data.csv"

RAW_SCRIPT_DATA_FPATH = os.path.join(_DATA_DIR, _RAW_SCRIPT_DATA_FNAME)
TRAIN_DATA_FPATH = os.path.join(_DATA_DIR, _TRAIN_DATA_FNAME)
DEV_DATA_FPATH = os.path.join(_DATA_DIR, _DEV_DATA_FNAME)
TEST_DATA_FPATH = os.path.join(_DATA_DIR, _TEST_DATA_FNAME)

RANDOM_SEED = 42

SANCHEZ_FAMILY_LABELS = {
    "Rick",
    "Morty",
    "Beth",
    "Jerry",
    "Summer",
}

macro_f1_score = partial(f1_score, average="macro")
micro_f1_score = partial(f1_score, average="micro")

SCORERS: Dict[str, Callable[[np.ndarray, np.ndarray], float]] = {
    "Accuracy": accuracy_score,
    "Macro F1": macro_f1_score,
    "Micro F1": micro_f1_score,
}

START_TOKEN = "<START>"
END_TOKEN = "<END>"

N_GRAMS_TO_COUNT = [1, 2, 3, 4]


WORD_CLUSTERS = {
    "Death": DEATH_WORDS,
    "Dubiety": DUBIETY_WORDS,
    "Sexual": SEXUAL_WORDS,
    "Condescension": CONDESCENSION_WORDS,
    "Intoxication": INTOXICATION_WORDS,
    "Gratitude": GRATITUDE_WORDS,
    "SciFi Creature": SCIFI_CREATURE_WORDS,
    "Generic Emotion": GENERIC_EMOTIION_WORDS,
    "Fancy Science": FANCY_SCIENCE_WORDS,
    "Food": FOOD_WORDS,
}


HAND_SELECTED_POS_BIGRAMS = {
    "'AUX VERB'",
    "'ADV PUNCT'",
    "'PUNCT DET'",
    "'ADV ADV'",
    "'VERB PRON'",
    "'PROPN PROPN'",
    "'PROPN NOUN'",
    "'SCONJ PRON'",
    "'ADJ PUNCT'",
    "'PUNCT PROPN'",
    "'ADV VERB'",
    "'DET ADJ'",
    "'AUX PRON'",
    "'NOUN PUNCT'",
    "'VERB ADP'",
    "'PRON VERB'",
    "'PROPN PUNCT'",
    "'AUX PART'",
    "'VERB PUNCT'",
    "'PRON ADV'",
    "'PRON NOUN'",
    "'PRON PUNCT'",
    "'ADP DET'",
    "'DET NOUN'",
    "'ADJ NOUN'",
    "'INTJ PUNCT'",
    "'PART VERB'",
    "'PUNCT PRON'",
    "'PUNCT INTJ'",
    "'VERB PROPN'",
    "'NOUN NOUN'",
    "'PUNCT VERB'",
    "'ADP VERB'",
    "'ADP PRON'",
    "'ADP PUNCT'",
    "'PRON PRON'",
    "'PRON AUX'",
}
HAND_SELECTED_POS_TRIGRAMS = {
    "'VERB PRON NOUN'",
    "'PRON ADP NOUN'",
    "'ADP ADJ PUNCT'",
    "'NOUN NOUN PUNCT'",
    "'NOUN PUNCT PROPN'",
    "'ADP PROPN PUNCT'",
    "'AUX DET ADJ'",
    "'ADP PRON NOUN'",
    "'PRON NOUN ADP'",
    "'VERB ADV SCONJ'",
    "'PROPN PROPN AUX'",
    "'DET NOUN PUNCT'",
    "'ADP PRON ADV'",
    "'PART VERB ADV'",
    "'PUNCT PRON PROPN'",
    "'INTJ PUNCT PRON'",
    "'PRON PUNCT PROPN'",
    "'AUX PART VERB'",
    "'ADP NOUN PUNCT'",
    "'PRON PROPN PUNCT'",
    "'AUX ADP PRON'",
    "'VERB PRON ADV'",
    "'VERB ADJ NOUN'",
    "'ADV ADV SCONJ'",
    "'VERB PART PUNCT'",
    "'NOUN PUNCT PUNCT'",
    "'PUNCT ADJ PUNCT'",
    "'PUNCT NOUN PUNCT'",
    "'PRON AUX VERB'",
    "'PUNCT PROPN PUNCT'",
    "'ADJ NOUN PUNCT'",
    "'PROPN PUNCT PRON'",
    "'AUX VERB VERB'",
    "'NOUN VERB NOUN'",
    "'ADP DET NOUN'",
    "'PROPN PUNCT PROPN'",
    "'PUNCT AUX PART'",
    "'PRON VERB ADP'",
    "'AUX PRON NOUN'",
    "'DET NOUN PRON'",
    "'PUNCT PRON VERB'",
    "'VERB PART VERB'",
    "'INTJ PUNCT NOUN'",
    "'PUNCT PRON AUX'",
    "'INTJ INTJ PROPN'",
}
