from typing import Protocol, List
import os
import pickle
import json
from functools import partial

import spacy
import pandas as pd

from src.globals import (
    NEIGHBORHOODS_FPATH,
    FEATURE_COLS_FPATH,
    MODEL_FPATH,
    FAMILIAL_WORDS_AND_COMMON_NAMES,
)
from src.feature_extractors import (
    avg_token_length,
    question_marks_per_sentence,
    exclamation_marks_per_sentence,
    dashes_per_sentence,
    all_n_gram_one_hots,
    get_counts_of_hand_selected_pos_n_grams,
    proportion_stop_words,
    proportion_alpha_chars_capitalized,
    neighborhood_degrees_of_presence,
)

assert os.path.exists(NEIGHBORHOODS_FPATH)
with open(NEIGHBORHOODS_FPATH, "r") as f:
    NEIGHBORHOODS = json.load(f)
LABEL_DECODER = {0: "Beth", 1: "Jerry", 2: "Morty", 3: "Rick", 4: "Summer"}
FEATURE_EXTRACTORS = {
    "Average Word Length": avg_token_length,
    "Question Marks Per Sentence": question_marks_per_sentence,
    "Exclamation Marks Per Sentence": exclamation_marks_per_sentence,
    "Dashes Per Sentence": dashes_per_sentence,
    "Familial Words & Common Names 1-Gram One Hots": partial(
        all_n_gram_one_hots, n=1, whitelist=FAMILIAL_WORDS_AND_COMMON_NAMES
    ),
    "Hand-Selected POS-Tag N-Gram Counts": get_counts_of_hand_selected_pos_n_grams,
    "Proportion Of Tokens That Are Stop Words": proportion_stop_words,
    "Proportion Of Chars That Are Capitalized": proportion_alpha_chars_capitalized,
    "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-wiki-gigaword-50)(Rndm)(-blacklist)": partial(
        neighborhood_degrees_of_presence,
        gensim_model_slug="glove-wiki-gigaword-50",
        weight_decay_rate=0.5,
        n_neighbors=5,
        lemmatize=True,
        max_top_n=4,
        neighborhoods=NEIGHBORHOODS,
    ),
}


class Model(Protocol):
    def predict(self, X) -> List[int]:
        ...


def get_features(text: str) -> List[float]:
    # Extract features from text
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    features = {}
    for extractor in FEATURE_EXTRACTORS.values():
        features.update(extractor(doc))
    # Create array of features in same order as in training
    with open(FEATURE_COLS_FPATH, "r") as f:
        feature_cols = json.load(f)
    features_array = {}
    for feature_name in feature_cols:
        if feature_name in features:
            features_array[feature_name] = features[feature_name]
        else:
            features_array[feature_name] = 0
    return pd.DataFrame([features_array], columns=feature_cols)


def run_inference(text: str) -> str:
    with open(MODEL_FPATH, "rb") as f:
        model: Model = pickle.load(f)
    features = get_features(text)
    prediction = model.predict(features)[0]
    return LABEL_DECODER[prediction]
