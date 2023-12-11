from collections import defaultdict
from functools import cache, partial
from typing import List

import spacy

from src.config import FEATURE_EXTRACTORS
from src.globals import BY_EPISODE_STR, RANDOM_STR
from src.helpers import load_data
from src.schema.configured_experiment import ConfiguredExperiment
from src.schema.experiment import Experiment


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
    rnd_train_test_dev, rnd_labels, rnd_utterances, rnd_previous_speakers = load_data(
        split_method=RANDOM_STR
    )
    epi_train_test_dev, epi_labels, epi_utterances, epi_previous_speakers = load_data(
        split_method=BY_EPISODE_STR
    )
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
        nlp = spacy.load(spacy_model_name)
        # Organize expirements by split method
        configured_experiments_by_use_by_episode_splits = defaultdict(list)
        for cnfg_exp in configured_experiments:
            configured_experiments_by_use_by_episode_splits[
                cnfg_exp.use_by_episode_splits
            ].append(cnfg_exp)
        # Iterate through split methods
        for (
            use_by_episode_splits,
            configured_experiments,
        ) in configured_experiments_by_use_by_episode_splits.items():
            labels = epi_labels if use_by_episode_splits else rnd_labels
            train_test_dev = (
                epi_train_test_dev if use_by_episode_splits else rnd_train_test_dev
            )
            previous_speakers = (
                epi_previous_speakers
                if use_by_episode_splits
                else rnd_previous_speakers
            )
            utterances = epi_utterances if use_by_episode_splits else rnd_utterances
            # Preprocess utterances with SpaCy
            docs = utterances.apply(lambda utterance: nlp(utterance))
            # Partialize feature extractors with docs and add caching
            caching_extractors = {}
            for name, feature_extractor in FEATURE_EXTRACTORS.items():
                if feature_extractor is None:
                    caching_extractors[name] = None
                else:
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
                        previous_speakers=previous_speakers,
                        feature_extractors=feature_extractors,
                        spacy_model_name=spacy_model_name,
                        use_by_episode_splits=use_by_episode_splits,
                    )
                )
    return initialized_experiments
