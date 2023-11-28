from typing import List
from functools import cache, partial
from collections import defaultdict
from time import perf_counter

import spacy

from src.helpers import load_data
from src.schema.configured_experiment import ConfiguredExperiment
from src.schema.experiment import Experiment
from src.config import FEATURE_EXTRACTORS


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
    print("🚀 Initializing experiments...")
    # Load data
    train_test_dev, labels, utterances = load_data()
    # Organize experiments by SpaCy model
    configured_experiments_by_spacy_model = defaultdict(list)
    for cnfg_exp in configured_experiments:
        configured_experiments_by_spacy_model[cnfg_exp.spacy_model_name].append(
            cnfg_exp
        )
    # Iterate through SpaCy models
    initialized_experiments = []
    for (
        spacy_model_name,
        configured_experiments,
    ) in configured_experiments_by_spacy_model.items():
        # Load SpaCy model
        start = perf_counter()
        nlp = spacy.load(spacy_model_name)
        spacy_model_load_time = perf_counter() - start
        # Preprocess utterances with SpaCy
        start = perf_counter()
        docs = utterances.apply(lambda utterance: nlp(utterance))
        preprocess_utterances_time = perf_counter() - start
        n_utterances = len(utterances)
        avg_utterance_preprocessing_time = preprocess_utterances_time / n_utterances
        # Partialize feature extractors with docs and add caching
        caching_extractors = {}
        for name, feature_extractor in FEATURE_EXTRACTORS.items():
            cachable_extractor = partial(feature_extractor, docs=docs)
            caching_extractors[name] = cache(cachable_extractor)
        # Initialize experiment objects
        for cnfg_exp in configured_experiments:
            feature_extractors = {
                name: extractor
                for name, extractor in caching_extractors.items()
                if name in cnfg_exp.feature_extractor_names
            }
            initialized_experiments.append(
                cnfg_exp.ExperimentType(
                    docs=docs,
                    labels=labels,
                    train_test_dev=train_test_dev,
                    spacy_model_name=spacy_model_name,
                    feature_extractors=feature_extractors,
                    spacy_model_load_time=spacy_model_load_time,
                    avg_utterance_preprocessing_time=avg_utterance_preprocessing_time,
                )
            )
    return initialized_experiments
