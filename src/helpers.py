from time import perf_counter

from typing import List, Tuple, Literal, Dict, Set
from functools import cache
from collections import defaultdict, Counter

from gensim.models import KeyedVectors
import gensim.downloader
import pandas as pd
import numpy as np

from src.globals import (
    TEST_DATA_FPATH,
    DEV_DATA_FPATH,
    TRAIN_DATA_FPATH,
    START_TOKEN,
    END_TOKEN,
    N_GRAMS_TO_COUNT,
)


@cache
def load_data() -> (
    Tuple[
        "pd.Series[Literal['train', 'test', 'dev']]",  # train/text/dev allocations
        "pd.Series[str]",  # speaker labels
        "pd.Series[str]",  # utterances
    ]
):
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
    train_df = pd.read_csv(TRAIN_DATA_FPATH)
    dev_df = pd.read_csv(DEV_DATA_FPATH)
    test_df = pd.read_csv(TEST_DATA_FPATH)
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
    return train_test_dev, labels, utterances


@cache
def load_embedding_model(slug: str) -> KeyedVectors:
    """Loads a gensim embedding model given its slug."""
    print(f"🔍 Loading gensim embedding model: {slug}")
    start = perf_counter()
    print(f"⌛ Loaded {slug} in {perf_counter() - start:.2f} seconds.")
    return gensim.downloader.load(slug)


@cache
def convert_text_to_n_grams(text: str, n: int) -> List[Tuple[str]]:
    """Converts a SpaCy Doc to a list of n-grams (after lowering & removing punctuation).

    Args:
        text (str): The text to convert to n-grams.
        n (int): The length of the n-grams.

    Returns:
        List[str]: A list of n-grams.
    """
    # no_punctuation = "".join([char for char in text if char.isalnum() or char == " "])
    lowered_tokens = text.lower().split()
    if n > 1:
        lowered_tokens = [START_TOKEN] + lowered_tokens
        lowered_tokens.append(END_TOKEN)
    n_grams = []
    for start_idx in range(len(lowered_tokens) - n + 1):
        n_gram = " ".join(lowered_tokens[start_idx : start_idx + n])
        n_grams.append(n_gram)
    return n_grams


@cache
def get_counts_by_speaker_by_n_gram_in_training_data() -> Dict[int, Dict[str, Counter]]:
    # FIXME: Docstring
    train_test_dev, labels, utterances = load_data()
    train_utterances = utterances[train_test_dev == "train"]
    n_grams_by_utterance_by_n = {}
    for n in N_GRAMS_TO_COUNT:
        n_grams_by_utterance_by_n[n] = train_utterances.apply(
            lambda doc: convert_text_to_n_grams(doc, n)
        )
    counts_by_speaker_by_n_gram = {}
    for n, n_grams_by_utterance in n_grams_by_utterance_by_n.items():
        counts_by_speaker = defaultdict(Counter)
        for speaker, n_grams in zip(labels, n_grams_by_utterance):
            counts_by_speaker[speaker].update(n_grams)
        counts_by_speaker_by_n_gram[n] = counts_by_speaker

    return counts_by_speaker_by_n_gram


# @cache
# def get_most_characteristic_n_grams_in_training_data(num: int, n: int) -> Set[str]:
#     """Uses custom 'TF-ISF' formula to determine the {num} most characteristic n-grams
#     for each speaker in the training data.

#     TF-IDF is a measure of originality of an n-gram to a document by comparing the
#     number of times an n-gram appears in a document with the number of documents the
#     n-gram appears in. Here, we adapt this formula to instead quantify the originality of
#     an n-gram to a speaker.

#     I.E. -- TF-ISF ("term frequency, inverse speaker frequency) = TF * ISF

#     Where:

#         TF = (
#             N times speaker has uttered the n-gram term
#             / N utterances of any n-gram by speaker
#         )

#         ISF = log(
#             N times any speaker has uttered the n-gram term
#             / N utterances of any n-gram by any speaker
#         )

#     Args:
#         num (int): The max number of most characteristic n-grams to extract per speaker.
#         n (int): The n-gram length.
#     """
#     counts_by_speaker = get_counts_by_speaker_by_n_gram_in_training_data()[n]

#     n_grams_counts_across_all_speakers = Counter()
#     for _, counts in counts_by_speaker.items():
#         n_grams_counts_across_all_speakers.update(counts)

#     tf_isf_by_speaker: Dict[str, Dict[int, str]] = {}
#     for speaker, counts in counts_by_speaker.items():
#         tf_isf_scores = {}
#         for n_gram, n_times_uttered_n_gram in counts.items():
#             # Calculate TF
#             tf = n_times_uttered_n_gram / sum(counts.values())
#             # Calculate ISF
#             n_times_uttered_all_speakers = n_grams_counts_across_all_speakers[n_gram]
#             isf = n_times_uttered_all_speakers / sum(
#                 n_grams_counts_across_all_speakers.values()
#             )
#             # Calculate TF-ISF
#             tf_isf_scores[n_gram] = tf * isf
#         tf_isf_by_speaker[speaker] = tf_isf_scores

#     most_characteristic_n_grams = set()
#     for speaker, tf_isf_scores in tf_isf_by_speaker.items():
#         for n_gram, _ in sorted(
#             tf_isf_scores.items(), key=lambda item: item[1], reverse=True
#         )[:num]:
#             most_characteristic_n_grams.add((n_gram))
#     return most_characteristic_n_grams


@cache
def get_most_characteristic_n_grams_in_training_data(num: int, n: int) -> Set[str]:
    # TODO: Docstring
    # Get counts of n-grams for each speaker
    counts_by_speaker = get_counts_by_speaker_by_n_gram_in_training_data()[n]
    # Pre-calculate normalized speaker frequencies
    speaker_freqs_by_speaker: Dict[str, Dict[str, float]] = {}
    for speaker, counts in counts_by_speaker.items():
        speaker_freqs = {}
        for n_gram, n_times_uttered_n_gram in counts.items():
            speaker_freq = n_times_uttered_n_gram / sum(counts.values())
            speaker_freqs[n_gram] = speaker_freq
        speaker_freqs_by_speaker[speaker] = speaker_freqs
    # Calculate originality scores and add the {num} highest to overall set
    most_characteristic_n_grams_in_training_data = set()
    for speaker, speaker_freqs in speaker_freqs_by_speaker.items():
        originality_scores = {}
        for n_gram, speaker_freq in speaker_freqs.items():
            # Get average speaker freq of n-gram across all other speakers
            non_speaker_speaker_freqs = []
            for speaker_2, speaker_freqs_2 in speaker_freqs_by_speaker.items():
                if speaker_2 == speaker:
                    continue
                if n_gram in speaker_freqs_2:
                    non_speaker_speaker_freqs.append(speaker_freqs_2[n_gram])
                else:  # N-gram not uttered by speaker
                    non_speaker_speaker_freqs.append(0)
            avg_speaker_freq_across_other_speakers = np.mean(non_speaker_speaker_freqs)
            # Compute n-gram originality score for current speaker
            originality_score = speaker_freq - avg_speaker_freq_across_other_speakers
            originality_scores[n_gram] = originality_score
        # Add the {num} highest originality scores to overall set
        for n_gram, _ in sorted(
            originality_scores.items(), key=lambda item: item[1], reverse=True
        )[:num]:
            most_characteristic_n_grams_in_training_data.add((n_gram))
    return most_characteristic_n_grams_in_training_data
