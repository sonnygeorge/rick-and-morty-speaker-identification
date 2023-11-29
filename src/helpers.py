from time import perf_counter
import os

from typing import List, Tuple, Literal, Dict, Set
from functools import cache

from gensim.models import KeyedVectors
import gensim.downloader
import pandas as pd
import numpy as np
from spacy.tokens import Doc

from src.globals import (
    TEST_STR,
    DEV_STR,
    TRAIN_STR,
    START_TOKEN,
    END_TOKEN,
    RANDOM_STR,
    BY_EPISODE_STR,
    DATA_DIR_PATH,
)


class RickPredictor:
    def fit(self, *args, **kwargs):
        pass

    def predict(self, X):
        return ["Rick"] * len(X)


@cache
def load_data(
    split_method: str = RANDOM_STR,
) -> Tuple[
    "pd.Series[Literal['train', 'test', 'dev']]",  # Train/dev/test allocations
    "pd.Series[str]",  # Speaker labels
    "pd.Series[str]",  # Utterances
]:
    """Loads the data from the data directory.

    Returns:
        Tuple[
            "pd.Series[Literal['train', 'test', 'dev']]",  # `train_test_dev`
            "pd.Series[str]",  # `labels`
            "pd.Series[str]",  # `utterances`
        ]:
        A tuple of pd.Series where respectively...
            - `train_test_dev`: a Series of strings indicating whether each utterance
              is in the train, dev, or test set.
            - `labels`:  a Series of strings indicating the speaker of each utterance.
            - `utterances`:  a Series of strings, one for each utterance.
    """
    train_df = pd.read_csv(
        os.path.join(DATA_DIR_PATH, f"{TRAIN_STR}_{split_method}.csv")
    )
    dev_df = pd.read_csv(os.path.join(DATA_DIR_PATH, f"{DEV_STR}_{split_method}.csv"))
    test_df = pd.read_csv(os.path.join(DATA_DIR_PATH, f"{TEST_STR}_{split_method}.csv"))
    train_test_dev = pd.concat(
        [
            pd.Series(["train"] * len(train_df)),
            pd.Series(["dev"] * len(dev_df)),
            pd.Series(["test"] * len(test_df)),
        ],
        ignore_index=True,
    )
    labels = pd.concat(
        [train_df["label"], dev_df["label"], test_df["label"]],
        ignore_index=True,
    )
    utterances = pd.concat(
        [train_df["utterance"], dev_df["utterance"], test_df["utterance"]],
        ignore_index=True,
    )
    previous_speakers = pd.concat(
        [
            train_df["previous speaker"],
            dev_df["previous speaker"],
            test_df["previous speaker"],
        ],
        ignore_index=True,
    )
    return train_test_dev, labels, utterances, previous_speakers


@cache
def load_embedding_model(slug: str) -> KeyedVectors:
    """Loads a gensim embedding model given its slug."""
    print(f"🔍 Loading gensim embedding model: {slug}")
    start = perf_counter()
    print(f"⌛ Loaded {slug} in {perf_counter() - start:.2f} seconds.")
    return gensim.downloader.load(slug)


@cache
def convert_doc_to_n_grams(
    doc: Doc,
    n: int,
    lemmatize: bool = False,
    append_depedency_labels: bool = False,
) -> List[Tuple[str]]:
    """Converts a SpaCy Doc to a list of n-grams.

    Args:
        doc (str): The SpaCy Doc to convert.
        n (int): The length of the n-grams.

    Returns:
        List[str]: A list of n-grams.
    """
    token_strings = []
    for token in doc:
        if token.is_punct:
            continue
        if token.is_stop:
            continue
        if token.is_space:
            continue
        if lemmatize:
            token_string = token.lemma_.lower()
        else:
            token_string = token.text.lower()
        if append_depedency_labels:
            token_string += f"_{token.dep_}"
        token_strings.append(token_string)
    # token_strings = doc.text.lower().split()
    if n > 1:
        token_strings = [START_TOKEN] + token_strings
        token_strings.append(END_TOKEN)
    n_grams = []
    for start_idx in range(len(token_strings) - n + 1):
        n_gram = " ".join(token_strings[start_idx : start_idx + n])
        n_grams.append(n_gram)
    return n_grams
