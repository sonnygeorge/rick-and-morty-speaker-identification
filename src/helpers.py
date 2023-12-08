from time import perf_counter
import os

from typing import List, Tuple, Literal, Dict, Union
from functools import cache

from gensim.models import KeyedVectors
import gensim.downloader
import pandas as pd
import numpy as np
from spacy.tokens import Doc
import spacy

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
        return [3] * len(X)  # Rick is encoded as 2


@cache
def get_exponentially_decaying_weights(n_weights: int, decay_rate: float) -> np.ndarray:
    """Returns an exponentially decaying array of weights that sum to one.

    Args:
        length (int): The length of the array.
        rate (float): The rate of decay.

    Returns:
        np.ndarray: An exponentially decaying array of weights that sum to one.
    """
    # Generate an array of n values using the exponential decay function
    x = np.arange(n_weights)
    weights = np.exp(-decay_rate * x)
    # Normalize the weights so they sum to one
    weights /= np.sum(weights)
    assert np.isclose(np.sum(weights), 1)
    return weights


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


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
) -> Union[List[Tuple[str]], List[str]]:
    """Converts a SpaCy Doc to a list of n-grams.

    Args:
        doc (str): The SpaCy Doc to convert.
        n (int): The length of the n-grams.

    Returns:
        List[str]: A list of n-grams.
    """
    all_n_grams = []
    for sent in doc.sents:
        token_strings = []
        for token in sent:
            if token.is_punct or token.is_stop or token.is_space:
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
        sent_n_grams = []
        for start_idx in range(len(token_strings) - n + 1):
            n_gram = " ".join(token_strings[start_idx : start_idx + n])
            sent_n_grams.append(n_gram)
        all_n_grams.extend(sent_n_grams)
    return sent_n_grams


@cache
def get_neighbors(
    word: str,
    gensim_model_slug: str,
    n_neighbors: int,
) -> List[Tuple[str, float]]:
    """Gets the n most similar words to the given word.

    Args:
        word (str): The word to find neighbors for.
        gensim_model_slug (str): The slug of the gensim model to use.
        n_neighbors (int): The number of neighbors to find.

    Returns:
        List[Tuple[str, float]]: A list of tuples of the form (neighbor, similarity).
    """
    model = load_embedding_model(gensim_model_slug)
    if word not in model:
        raise ValueError(f"Word '{word}' not in model: {gensim_model_slug}.")
    return model.most_similar(positive=[word], topn=n_neighbors)


@cache
def get_neighborhoods_from_training_data(
    use_by_episode_split: bool,
    lemmatize: bool,
    n_neighbors: int,
    gensim_model_slug: str,
) -> Dict[str, np.ndarray]:
    # TODO: Docstring
    if use_by_episode_split:
        train_test_dev, _, utterances, _ = load_data(split_method=BY_EPISODE_STR)
    else:
        train_test_dev, _, utterances, _ = load_data(split_method=RANDOM_STR)
    utterances = utterances[train_test_dev == TRAIN_STR]
    model = load_embedding_model(gensim_model_slug)
    nlp = spacy.load("en_core_web_sm")
    docs: "pd.Series[Doc]" = utterances.apply(nlp)
    neighborhoods = {}
    for doc in docs:
        for token in doc:
            if token.is_stop or token.is_punct or token.is_space:
                continue
            if lemmatize:
                token_string = token.lemma_.lower()
            else:
                token_string = token.text.lower()
            if token_string not in neighborhoods:
                if token_string not in model:
                    continue
                neighbors = get_neighbors(
                    token_string,
                    gensim_model_slug=gensim_model_slug,
                    n_neighbors=n_neighbors,
                )
                neighbor_vecs = [model[neighbor] for neighbor, _ in neighbors]
                mean_neighbor_vec = np.mean(neighbor_vecs, axis=0)
                neighborhoods[token_string] = mean_neighbor_vec
    return neighborhoods
