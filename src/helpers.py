from typing import List, Tuple, Literal
from functools import cache, partial
from collections import defaultdict
from time import perf_counter

import pandas as pd
import numpy as np
import spacy
from spacy.tokens import Doc
from spacy.language import Language

from src.globals import DATA_FPATH, SANCHEZ_FAMILY, ENABLED_SPACY_COMPONENTS
from src.configured_experiment import ConfiguredExperiment
from src.experiment import Experiment
from src.config import FEATURE_EXTRACTORS


def load_data() -> Tuple["pd.Series[str]", "pd.Series[str]"]:
    """Reads in Rick and Morty script data, filters it to the Sanchez family, and returns
    the utterances and speakers as Series.

    Returns:
        Tuple[pd.Series[str], pd.Series[str]]: A tuple containing the utterances and
            speakers respectively as Series.
    """
    df = pd.read_csv(DATA_FPATH)
    df = df[df["speaker"].isin(SANCHEZ_FAMILY)]
    X, y = df["utterance"], df["speaker"]
    return X, y


def create_splits(index: pd.Index) -> "pd.Series[Literal['train', 'dev', 'test']]":
    """
    Randomly assigns 'train', 'dev', or 'test' to each element of a pandas Series index.

    Args:
        index (pd.Index): The index of a pandas Series.

    Returns:
        pd.Series: A Series with the same index, with labels 'train', 'dev', or 'test'.
    """
    labels = np.random.choice(["train", "dev", "test"], size=len(index))
    return pd.Series(labels, index=index)


def preprocess_spacy_doc(
    nlp: Language,
    input_text: str,
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
    train_dev_test_split = create_splits(utterances.index)
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
                Experiment(
                    model_type=configured_experiment.Experiment,
                    feature_extractors=caching_extractors,
                    docs=docs,
                    labels=labels,
                    train_dev_test_split=train_dev_test_split,
                    model_load_time=model_load_time,
                    avg_utterance_preprocessing_time=avg_utterance_preprocessing_time,
                )
            )
    return initialized_experiments
