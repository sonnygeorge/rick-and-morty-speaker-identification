from typing import List, Tuple, Literal
from functools import cache, partial
from collections import defaultdict
from time import perf_counter

import pandas as pd
import numpy as np
import spacy
from spacy.tokens import Doc
from spacy.language import Language
from sklearn.model_selection import train_test_split

from src.globals import (
    DATA_FPATH,
    SANCHEZ_FAMILY_LABELS,
    ENABLED_SPACY_COMPONENTS,
    SPLIT_RATIOS,
    SEED,
)
from src.schema.configured_experiment import ConfiguredExperiment
from src.schema.experiment import Experiment
from src.config import FEATURE_EXTRACTORS


def load_data() -> Tuple["pd.Series[str]", "pd.Series[str]"]:
    """Reads in Rick and Morty script data, filters it to the Sanchez family, and returns
    the utterances and speakers as Series.

    Returns:
        Tuple[pd.Series[str], pd.Series[str]]: A tuple containing the utterances and
            speakers respectively as Series.
    """
    df = pd.read_csv(DATA_FPATH)
    df = df[df["name"].isin(SANCHEZ_FAMILY_LABELS)]
    X, y = df["line"], df["name"]
    return X, y


def create_splits(index: pd.Index) -> "pd.Series[Literal['train', 'dev', 'test']]":
    """
    Randomly assigns 'train', 'dev', or 'test' to each element of a pandas Series index
    according to the partition ratios defined in `SPLIT_RATIOS`.

    Args:
        index (pd.Index): The index of a pandas Series.

    Returns:
        pd.Series: A Series with the same index, with labels 'train', 'dev', or 'test'.
    """
    # Split between train and the rest
    train_index, rest_index = train_test_split(
        index,
        test_size=SPLIT_RATIOS["test"] + SPLIT_RATIOS["dev"],
        shuffle=True,
        random_state=SEED,
    )
    # Adjust dev ratio to account for the fact that we already split off test
    ratio = SPLIT_RATIOS["dev"] / (SPLIT_RATIOS["dev"] + SPLIT_RATIOS["test"])
    # Second split between test and dev
    test_index, dev_index = train_test_split(
        rest_index, test_size=ratio, shuffle=True, random_state=SEED
    )

    # Create the final Series with labels
    labels = pd.Series(index=index, dtype="object")
    labels[train_index] = "train"
    labels[test_index] = "test"
    labels[dev_index] = "dev"
    return labels


def preprocess_spacy_doc(
    input_text: str,
    nlp: Language,
) -> Doc:
    """Applies SpaCy preprocessing to the input text and returns the processed Doc.

    Args:
        nlp (Language): A SpaCy Language object.
        input_text (str): The input text to be processed.
        enabled_components (List[str]): A list of pipeline components to be enabled.

    Returns:
        Doc: The processed SpaCy Doc object.
    """
    disabled = [c for c in nlp.pipe_names if c not in ENABLED_SPACY_COMPONENTS]
    with nlp.disable_pipes(disabled):
        doc = nlp(input_text)
    return doc


def initialize_experiments(
    configured_experiments: List[ConfiguredExperiment],
) -> List[Experiment]:
    """Initializes a list of experiments with the given configured experiments.

    Args:
        configured_experiments (List[ConfiguredExperiment]): A list of configured
            experiments.

    Returns:
        List[Experiment]: A list of initialized experiment objects.
    """
    utterances, labels = load_data()
    train_test_dev = create_splits(utterances.index)
    # Print number of uterrances per speaker per split
    for split in ["train", "dev", "test"]:
        print(f"Number of utterances per speaker in {split} split:")
        print(labels[train_test_dev == split].value_counts())
    # Organize experiments by SpaCy model
    configured_experiments_by_spacy_model = defaultdict(list)
    for configured_experiment in configured_experiments:
        configured_experiments_by_spacy_model[
            configured_experiment.spacy_model_name
        ].append(configured_experiment)
    # Iterate through SpaCy models
    initialized_experiments = []
    for (
        spacy_model_name,
        configured_experiments,
    ) in configured_experiments_by_spacy_model.items():
        # Load SpaCy model
        start = perf_counter()
        nlp = spacy.load(spacy_model_name)
        model_load_time = perf_counter() - start
        # Preprocess utterances with SpaCy
        start = perf_counter()
        docs = utterances.apply(preprocess_spacy_doc, nlp=nlp)
        preprocess_utterances_time = perf_counter() - start
        n_utterances = len(utterances)
        avg_utterance_preprocessing_time = preprocess_utterances_time / n_utterances
        # Partialize feature extractors with docs and add caching
        caching_extractors = {}
        for name, feature_extractor in FEATURE_EXTRACTORS.items():
            cachable_extractor = partial(feature_extractor, docs=docs)
            caching_extractors[name] = cache(cachable_extractor)
        # Initialize experiment objects
        for configured_experiment in configured_experiments:
            initialized_experiments.append(
                configured_experiment.Experiment(
                    docs=docs,
                    labels=labels,
                    train_test_dev=train_test_dev,
                    spacy_model_name=spacy_model_name,
                    feature_extractors=caching_extractors,
                    model_load_time=model_load_time,
                    avg_utterance_preprocessing_time=avg_utterance_preprocessing_time,
                )
            )
    return initialized_experiments
