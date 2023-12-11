import os
from functools import partial
from typing import Callable, Dict

import numpy as np
from sklearn.metrics import accuracy_score, f1_score

from src.word_clusters import (CONDESCENSION_WORDS, DEATH_WORDS, DUBIETY_WORDS,
                               FANCY_SCIENCE_WORDS, FOOD_WORDS,
                               GENERIC_EMOTIION_WORDS, GRATITUDE_WORDS,
                               INTOXICATION_WORDS, SCIFI_CREATURE_WORDS,
                               SEXUAL_WORDS)

DATA_DIR_PATH = "data"
RAW_SCRIPT_DATA_FNAME = "RickAndMortyScripts.csv"
TRAIN_STR = "train"
DEV_STR = "dev"
TEST_STR = "test"
RANDOM_STR = "random"
BY_EPISODE_STR = "by_episode"
RESULTS_CSV_FNAME = "results.csv"

RAW_SCRIPT_DATA_FPATH = os.path.join(DATA_DIR_PATH, RAW_SCRIPT_DATA_FNAME)
RESULTS_CSV_FPATH = os.path.join(DATA_DIR_PATH, RESULTS_CSV_FNAME)


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

# Highly specific tokens that to my intuition/domain knowledge...
# ...seem likely to cause overfitting to the training data
TOKEN_BLACKLIST = {
    "d",
    "c",
    "yyyyyyyyyyou",
    "vindicator",
    "vindicators",
    "Vindicator",
    "Vindicators",
    "Paul",
    "paul",
    "Newman",
    "newman",
    "Goldenfold",
    "goldenfold",
    "Supernova",
    "supernova",
    "Gazorpazorp",
    "gazorpazorp",
    "Vagina",
    "vagina",
    "iii",
    "5",
    "squanch",
    "Cervine",
    "cervine",
    "ya",
    "yes",
    "yeah",
}  # AKA these are sus...

# Unigrams that won't embed well, so neighborhood degree of presence will be less...
# ...meaningful than unigram one-hots or counts
FAMILIAL_WORDS_AND_COMMON_NAMES = {
    "birdperson",
    "tammy",
    "gearhead",
    "jessica",
    "rick",
    "morty",
    "summer",
    "beth",
    "jerry",
    "wong",
    "smith",
    "sanchez",
    "sanchezes",
    "smiths",
    "father",
    "mother",
    "dad",
    "mom",
    "son",
    "daughter",
    "brother",
    "sister",
    "grandfather",
    "grandpa",
    "grandma",
    "mom",
    "dad",
    "sis",
    "bro",
    "grandmother",
    "grandson",
    "granddaughter",
    "jesus",
    "christ",
    "um",
    "uh",
    "married",
    "grampa",
    "honey",
    "you",
    "i",
    "me",
    "our",
    "your",
    "we",
    "my",
    "parent",
    "parents",
    "wife",
    "husband",
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
