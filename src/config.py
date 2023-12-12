import random
from functools import partial
from typing import Dict, List, Union

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

from src.feature_extractors import (all_n_gram_counts, all_n_gram_one_hots,
                                    avg_root_verb_embedding, avg_token_length,
                                    avg_tokens_per_sentence,
                                    dashes_per_sentence,
                                    exclamation_marks_per_sentence,
                                    get_counts_of_hand_selected_pos_n_grams,
                                    neighborhood_degrees_of_presence,
                                    pos_tag_n_gram_counts,
                                    proportion_alpha_chars_capitalized,
                                    proportion_stop_words,
                                    question_marks_per_sentence,
                                    topical_proximity_score,
                                    total_sentence_count)
from src.globals import FAMILIAL_WORDS_AND_COMMON_NAMES, RANDOM_SEED
from src.helpers import RickPredictor
from src.schema.configured_experiment import ConfiguredExperiment
from src.schema.feature_extractor import FeatureExtractor

random.seed(RANDOM_SEED)

_GENSIM_FEATURE_EXTRACTORS = {
    "Topical Proximity - Dubiety ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Dubiety",
    ),
    "Topical Proximity - Death ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Death",
    ),
    "Topical Proximity - Sexual ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Sexual",
    ),
    "Topical Proximity - Condescension ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Condescension",
    ),
    "Topical Proximity - Intoxication ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Intoxication",
    ),
    "Topical Proximity - Gratitude ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Gratitude",
    ),
    "Topical Proximity - SciFi Creature ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="SciFi Creature",
    ),
    "Topical Proximity - Generic Emotion ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Generic Emotion",
    ),
    "Topical Proximity - Fancy Science ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Fancy Science",
    ),
    "Topical Proximity - Food ({gensim_model})": partial(
        topical_proximity_score,
        topic_cluster="Food",
    ),
    "Nghbhood Degrees - Lemmas (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Full Tokens (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        lemmatize=False,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,4topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        max_top_n=4,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        max_top_n=1,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        weight_decay_rate=0.5,
        n_neighbors=5,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        weight_decay_rate=0.5,
        max_top_n=4,
        n_neighbors=5,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        weight_decay_rate=0.5,
        max_top_n=1,
        n_neighbors=5,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,no-topn,8nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=8,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,4topn,8nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=8,
        max_top_n=4,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,1topn,8nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=8,
        max_top_n=1,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,no-topn,8nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        weight_decay_rate=0.5,
        n_neighbors=8,
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,4topn,8nghbrs)({gensim_model})(Rndm){blacklist}": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        weight_decay_rate=0.5,
        max_top_n=4,
        n_neighbors=8,
        lemmatize=True,
    ),
    "Average Root Verb Embedding ({gensim_model})": partial(avg_root_verb_embedding),
}

GENERATION_GENSIM_PARAMS = [
    (0.3, "glove-twitter-25"),
    (0.2, "glove-twitter-50"),
    (0.2, "glove-wiki-gigaword-50"),
    (0.3, "fasttext-wiki-news-subwords-300"),
]

# Hydrate gensim feature extractors with gensim model slugs
GENSIM_FEATURE_EXTRACTORS = {}
for _, gensim_model in GENERATION_GENSIM_PARAMS:
    for name, feature_extractor in _GENSIM_FEATURE_EXTRACTORS.items():
        if "{blacklist}" in name:
            for use_blacklist, blacklist_string in [
                (False, ""),
                (True, "(-blacklist)"),
            ]:
                new_name = name.format(
                    gensim_model=gensim_model, blacklist=blacklist_string
                )
                new_fe = partial(
                    feature_extractor,
                    gensim_model_slug=gensim_model,
                    use_blacklist=use_blacklist,
                )
                GENSIM_FEATURE_EXTRACTORS[new_name] = new_fe
        else:
            new_name = name.format(gensim_model=gensim_model)
            new_fe = partial(feature_extractor, gensim_model_slug=gensim_model)
            GENSIM_FEATURE_EXTRACTORS[new_name] = new_fe


OTHER_FEATURE_EXTRACTORS: Dict[str, FeatureExtractor] = {
    # "Length features"
    "Total Sentence Count": total_sentence_count,
    "Average Tokens Per Sentence": avg_tokens_per_sentence,
    "Average Word Length": avg_token_length,
    # Prevalance of different punctuation marks
    "Question Marks Per Sentence": question_marks_per_sentence,
    "Exclamation Marks Per Sentence": exclamation_marks_per_sentence,
    "Dashes Per Sentence": dashes_per_sentence,
    # N-Gram One Hots
    "Familial Words & Common Names 1-Gram One Hots": partial(
        all_n_gram_one_hots, n=1, whitelist=FAMILIAL_WORDS_AND_COMMON_NAMES
    ),
    "All 1-Gram One Hots": partial(all_n_gram_one_hots, n=1),
    "All 1-Gram One Hots (-blacklist)": partial(
        all_n_gram_one_hots, n=1, use_blacklist=True
    ),
    "All 2-Gram One Hots": partial(all_n_gram_one_hots, n=2),
    # Lemmatized N-Gram One Hots
    "All 1-Gram One Hots (Lemmatized)": partial(
        all_n_gram_one_hots, n=1, lemmatize=True
    ),
    "All 2-Gram One Hots (Lemmatized)": partial(
        all_n_gram_one_hots, n=2, lemmatize=True
    ),
    # N-Gram One Hots With Dependency Labels
    "All 1-Gram One Hots (With Dependency Labels)": partial(
        all_n_gram_one_hots, n=1, append_depedency_labels=True
    ),
    "All 2-Gram One Hots (With Dependency Labels)": partial(
        all_n_gram_one_hots, n=2, append_depedency_labels=True
    ),
    # N-Gram Counts
    "Familial Words & Common Names 1-Gram Counts": partial(
        all_n_gram_counts, n=1, whitelist=FAMILIAL_WORDS_AND_COMMON_NAMES
    ),
    "All 1-Gram Counts": partial(all_n_gram_counts, n=1),
    "All 1-Gram Counts (-blacklist)": partial(
        all_n_gram_counts, n=1, use_blacklist=True
    ),
    "All 2-Gram Counts": partial(all_n_gram_counts, n=2),
    # Lemmatized N-Gram Counts
    "All 1-Gram Counts (Lemmatized)": partial(all_n_gram_counts, n=1, lemmatize=True),
    "All 2-Gram Counts (Lemmatized)": partial(all_n_gram_counts, n=2, lemmatize=True),
    # Normalized N-Gram Counts
    "All 1-Gram Counts (Normalized)": partial(all_n_gram_counts, n=1, normalize=True),
    "All 2-Gram Counts (Normalized)": partial(all_n_gram_counts, n=2, normalize=True),
    # Lemmatized & Normalized N-Gram Counts
    "All 1-Gram Counts (Lemmatized & Normalized)": partial(
        all_n_gram_counts, n=1, lemmatize=True, normalize=True
    ),
    "All 2-Gram Counts (Lemmatized & Normalized)": partial(
        all_n_gram_counts, n=2, lemmatize=True, normalize=True
    ),
    # POS-Tag N-Gram Counts
    "Hand-Selected POS-Tag N-Gram Counts": get_counts_of_hand_selected_pos_n_grams,
    "POS-Tag 1-Gram Counts": partial(pos_tag_n_gram_counts, n=1),
    "POS-Tag 2-Gram Counts": partial(pos_tag_n_gram_counts, n=2),
    "POS-Tag 3-Gram Counts": partial(pos_tag_n_gram_counts, n=3),
    # Other
    "Proportion Of Tokens That Are Stop Words": proportion_stop_words,
    "Proportion Of Chars That Are Capitalized": proportion_alpha_chars_capitalized,
    # Previous speaker (no feature extractor since this is manually achieved by the experiment)
    "Previous Speaker": None,
}

FEATURE_EXTRACTORS = {**OTHER_FEATURE_EXTRACTORS, **GENSIM_FEATURE_EXTRACTORS}
print("Number of unique feature extractors:", len(FEATURE_EXTRACTORS))

GENERATION_FEATURE_PARAMS = [
    (0.35, [(1.0, "Total Sentence Count")]),
    (0.95, [(1.0, "Average Tokens Per Sentence")]),
    (0.95, [(1.0, "Average Word Length")]),
    (0.95, [(1.0, "Question Marks Per Sentence")]),
    (0.95, [(1.0, "Exclamation Marks Per Sentence")]),
    (0.95, [(1.0, "Dashes Per Sentence")]),
    (0.95, [(1.0, "Proportion Of Tokens That Are Stop Words")]),
    (0.95, [(1.0, "Proportion Of Chars That Are Capitalized")]),
    (0.55, [(1.0, "Average Root Verb Embedding ({gensim_model})")]),
    (
        0.96,
        [
            (
                0.4,
                [
                    (0.1, "All 1-Gram One Hots (Lemmatized)"),
                    (0.17, "All 1-Gram One Hots"),
                    (0.17, "All 1-Gram One Hots (-blacklist)"),
                    (0.06, "All 1-Gram One Hots (With Dependency Labels)"),
                    (0.8, "All 1-Gram Counts"),
                    (0.9, "All 1-Gram Counts (-blacklist)"),
                    (0.17, "All 1-Gram Counts (Lemmatized)"),
                    (0.08, "All 1-Gram Counts (Normalized)"),
                    (0.08, "All 1-Gram Counts (Lemmatized & Normalized)"),
                ],
            ),
            (
                0.3,
                [
                    (
                        0.05,
                        "Nghbhood Degrees - Lemmas (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.02,
                        "Nghbhood Degrees - Full Tokens (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.13,
                        "Nghbhood Degrees - Lemmas (no-decay,4topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.18,
                        "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.7,
                        "Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.3,
                        "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.25,
                        "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.05,
                        "Nghbhood Degrees - Lemmas (no-decay,no-topn,8nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.02,
                        "Nghbhood Degrees - Lemmas (no-decay,4topn,8nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.13,
                        "Nghbhood Degrees - Lemmas (no-decay,1topn,8nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.18,
                        "Nghbhood Degrees - Lemmas (.5decay,no-topn,8nghbrs)({gensim_model})(Rndm)",
                    ),
                    (
                        0.7,
                        "Nghbhood Degrees - Lemmas (.5decay,4topn,8nghbrs)({gensim_model})(Rndm)",
                    ),
                ],
            ),
            (
                0.3,
                [
                    (
                        0.05,
                        "Nghbhood Degrees - Lemmas (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.02,
                        "Nghbhood Degrees - Full Tokens (no-decay,no-topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.13,
                        "Nghbhood Degrees - Lemmas (no-decay,4topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.18,
                        "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.7,
                        "Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.3,
                        "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.35,
                        "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.05,
                        "Nghbhood Degrees - Lemmas (no-decay,no-topn,8nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.02,
                        "Nghbhood Degrees - Lemmas (no-decay,4topn,8nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.16,
                        "Nghbhood Degrees - Lemmas (no-decay,1topn,8nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.19,
                        "Nghbhood Degrees - Lemmas (.5decay,no-topn,8nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                    (
                        0.8,
                        "Nghbhood Degrees - Lemmas (.5decay,4topn,8nghbrs)({gensim_model})(Rndm)(-blacklist)",
                    ),
                ],
            ),
        ],
    ),
    (0.07, [(1.0, "Topical Proximity - Dubiety ({gensim_model})")]),
    (0.07, [(1.0, "Topical Proximity - Death ({gensim_model})")]),
    (0.1, [(1.0, "Topical Proximity - Sexual ({gensim_model})")]),
    (0.13, [(1.0, "Topical Proximity - Condescension ({gensim_model})")]),
    (0.13, [(1.0, "Topical Proximity - Intoxication ({gensim_model})")]),
    (0.12, [(1.0, "Topical Proximity - Gratitude ({gensim_model})")]),
    (0.05, [(1.0, "Topical Proximity - SciFi Creature ({gensim_model})")]),
    (0.08, [(1.0, "Topical Proximity - Generic Emotion ({gensim_model})")]),
    (0.13, [(1.0, "Topical Proximity - Fancy Science ({gensim_model})")]),
    (0.08, [(1.0, "Topical Proximity - Food ({gensim_model})")]),
    (
        0.14,
        [
            (0.25, "All 2-Gram One Hots"),
            (0.2, "All 2-Gram One Hots (Lemmatized)"),
            (0.05, "All 2-Gram One Hots (With Dependency Labels)"),
            (0.225, "All 2-Gram Counts"),
            (0.125, "All 2-Gram Counts (Lemmatized)"),
            (0.075, "All 2-Gram Counts (Normalized)"),
            (0.075, "All 2-Gram Counts (Lemmatized & Normalized)"),
        ],
    ),
    (0.1, [(1.0, "Hand-Selected POS-Tag N-Gram Counts")]),
    (0.02, [(1.0, "POS-Tag 1-Gram Counts")]),
    (0.01, [(1.0, "POS-Tag 2-Gram Counts")]),
    (0.01, [(1.0, "POS-Tag 3-Gram Counts")]),
]


# Lazily thrown here to use specifically as an `eval_metric`` for XGBoost."""
def f1_macro(preds, dtrain):
    labels = dtrain.get_label()
    preds = preds.reshape(-1, 5)  # Reshape predictions (5 classes)
    preds = preds.argmax(axis=1)  # Take the argmax to get prediction labels
    f1 = f1_score(labels, preds, average="macro")
    return "macroF1", f1


GENERATION_MODEL_PARAMS = [
    (
        0.01,
        DecisionTreeClassifier,
        {
            "criterion": [(0.6, "gini"), (0.2, "entropy"), (0.2, "log_loss")],
            "max_depth": [
                (0.1, 3),
                (0.2, 4),
                (0.25, 5),
                (0.25, 8),
                (0.1, 11),
                (0.05, 15),
                (0.05, 20),
            ],
            "random_state": [(1.0, RANDOM_SEED)],
        },
    ),
    (
        1.1,
        XGBClassifier,
        {
            "random_state": [(1.0, RANDOM_SEED)],
            "max_depth": [
                (0.1, 3),
                (0.4, 4),
                (0.35, 5),
                (0.1, 6),
                (0.05, 7),
                (0.05, 11),
            ],
            "objective": [(0.5, "multi:softmax"), (0.5, "multi:softprob")],
            "num_class": [(1, 5)],
            "n_estimators": [
                (0.2, 23),
                (0.2, 35),
                (0.2, 45),
                (0.1, 60),
                (0.1, 80),
                (0.2, 100),
                (0.2, 137),
            ],
            # Minimum sum of instance weight needed in a child
            "min_child_weight": [(0.5, 1), (0.3, 2), (0.1, 3), (0.1, 4)],
            # Minimum loss reduction required to make a further partition on a leaf node
            "gamma": [(0.3, 0.05), (0.3, 0.1), (0.1, 0.2), (0.1, 0.3), (0.1, 0.4)],
            # Subsample ratio of the training instances
            "subsample": [(0.1, 0.5), (0.1, 0.6), (0.1, 0.8), (0.5, 0.8), (0.1, 0.9)],
            # Subsample ratio of columns when constructing each tree
            "colsample_bytree": [
                (0.1, 0.5),
                (0.1, 0.6),
                (0.1, 0.8),
                (0.5, 0.8),
                (0.1, 0.9),
            ],
            # L2 regularization term on weights
            "reg_lambda": [(0.1, 0.6), (0.1, 0.8), (0.6, 1), (0.2, 1.4)],
            # L1 regularization term on weights
            "reg_alpha": [(0.7, 0.1), (0.15, 0.3), (0.15, 5)],
            "learning_rate": [
                (0.3, 0.1),
                (0.2, 0.2),
                (0.2, 0.3),
                (0.2, 0.4),
                (0.1, 0.5),
            ],
            # L1 regularization
            "alpha": [(0.2, 0.5), (0.3, 0.8), (0.3, 1.2), (0.2, 1.8)],
            # ...
            "booster": [(0.5, "gbtree"), (0.4, "gblinear"), (0.1, "dart")],
            "eta": [(0.2, 0.15), (0.2, 0.2), (0.2, 0.3), (0.2, 0.4), (0.2, 0.55)],
            "eval_metric": [
                (0.3, f1_macro),
                (0.3, "mlogloss"),
                (0.3, "map"),
                (0.1, "mphe"),
            ],
        },
    ),
    (
        0.03,
        RandomForestClassifier,
        {
            "n_estimators": [(0.2, 45), (0.2, 60), (0.3, 80), (0.2, 140), (0.1, 220)],
            "criterion": [(0.6, "gini"), (0.2, "entropy"), (0.2, "log_loss")],
            "max_depth": [
                (0.15, 3),
                (0.25, 4),
                (0.25, 5),
                (0.25, 8),
                (0.5, 11),
                (0.05, 13),
            ],
            "random_state": [(1.0, RANDOM_SEED)],
        },
    ),
    (
        0.06,
        GradientBoostingClassifier,
        {
            "n_estimators": [(0.2, 45), (0.2, 60), (0.3, 80), (0.2, 140), (0.1, 220)],
            "learning_rate": [
                (0.2, 0.1),
                (0.2, 0.2),
                (0.2, 0.3),
                (0.2, 0.4),
                (0.2, 0.5),
            ],
            "max_depth": [
                (0.15, 3),
                (0.25, 4),
                (0.25, 5),
                (0.25, 8),
                (0.5, 11),
                (0.05, 13),
            ],
            "random_state": [(1.0, RANDOM_SEED)],
        },
    ),
    (
        0.9,
        LogisticRegression,
        {
            "penalty": [(0.3, "l1"), (0.3, "l2"), (0.4, "elasticnet")],
            "C": [(0.1, 0.5), (0.2, 0.7), (0.32, 1.0), (0.3, 1.5), (0.08, 1.8)],
            "solver": [(0.2, "lbfgs"), (0.2, "liblinear"), (0.6, "saga")],
            "random_state": [(1.0, RANDOM_SEED)],
        },
    ),
    (
        0.0,
        GaussianNB,
        {
            "var_smoothing": [
                (0.2, 1e-9),
                (0.2, 1e-8),
                (0.2, 1e-7),
                (0.2, 1e-6),
                (0.2, 1e-5),
            ],
        },
    ),
]


def generate_experiments(n: int) -> List[ConfiguredExperiment]:
    """Generates n experiments using the generation parameters defined above."""

    def _select_from_group(group: List[Union[tuple, list]]) -> Union[tuple, list]:
        """Probabilistically select an item from a generation parameter group."""
        weights = [item[0] for item in group]
        selected_item = random.choices(group, weights=weights, k=1)[0]
        return selected_item

    def _add_noise_to_value(val: Union[int, float, str]):
        if not isinstance(val, int) and not isinstance(val, float):
            return val
        is_int = isinstance(val, int)
        percent_addition = random.choice([0.1, 0.0, 0.0, 0.1, 0.15, 0.2, 0.29])
        adjustment_is_negative = random.random() < 0.5
        addition = val * percent_addition
        if adjustment_is_negative:
            addition *= -1
        if is_int:
            return val + int(addition)
        else:
            return np.round(val + addition, 2)

    experiments = []
    for _ in range(n):
        # Build a set of feature extractors
        feature_combo = []
        for prob, feature_extractor_group in GENERATION_FEATURE_PARAMS:
            if random.random() > prob:
                continue
            selection = _select_from_group(feature_extractor_group)
            if isinstance(selection[1], list):
                selection = _select_from_group(selection[1])
            feature_extractor_name: str = selection[1]
            if "gensim_model" in feature_extractor_name:
                gensim_model_slug = _select_from_group(GENERATION_GENSIM_PARAMS)[1]
                feature_extractor_name = feature_extractor_name.format(
                    gensim_model=gensim_model_slug
                )
            if feature_extractor_name not in FEATURE_EXTRACTORS:
                raise ValueError(  # Likely due to slight mismatch in manually typed string
                    f"Feature extractor {feature_extractor_name} not found in `FEATURE_EXTRACTORS`."
                )
            feature_combo.append(feature_extractor_name)
        if any("Nghbhood Degrees" in fe_name for fe_name in feature_combo):
            p_add_familial_words = 0.95
            if random.random() < p_add_familial_words:
                p_one_hots = 0.5
                if random.random() < p_one_hots:
                    feature_combo.append(
                        "Familial Words & Common Names 1-Gram One Hots"
                    )
                else:
                    feature_combo.append("Familial Words & Common Names 1-Gram Counts")
        # Generate model/model params
        selection = _select_from_group(GENERATION_MODEL_PARAMS)
        model_type = selection[1]
        model_kwargs = {}
        for param_name, param_group in selection[2].items():
            param_value = _select_from_group(param_group)[1]
            if param_name != "num_class":
                param_value = _add_noise_to_value(param_value)
            model_kwargs[param_name] = param_value
        # Manually avoid some impossible parameter combinations
        if model_type == LogisticRegression:
            model_kwargs["max_iter"] = 1400
            if model_kwargs["solver"] == "lbfgs":
                model_kwargs["penalty"] = "l2"
            if all(
                [
                    model_kwargs["solver"] == "liblinear",
                    model_kwargs["penalty"] == "elasticnet",
                ]
            ):
                model_kwargs["penalty"] = "l2"
            if model_kwargs["penalty"] == "elasticnet":
                model_kwargs["l1_ratio"] = 0.5
        # Append generated experiment
        experiment = ConfiguredExperiment(
            feature_extractor_names=feature_combo,
            spacy_model_name="en_core_web_sm",
            use_by_episode_splits=False,
            model_type=model_type,
            **model_kwargs,
        )
        experiments.append(experiment)
    return experiments


BASELINE_EXPERIMENTS: List[ConfiguredExperiment] = [
    ConfiguredExperiment(
        feature_extractor_names=["Total Sentence Count"],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=RickPredictor,
    ),
    ConfiguredExperiment(
        feature_extractor_names=["All 1-Gram One Hots"],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=LogisticRegression,
        penalty="l2",
        C=0.7,
        solver="saga",
        max_iter=1400,
        random_state=RANDOM_SEED,
    ),
]

MANUALLY_CONFIGURED_EXPERIMENTS = [
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-wiki-gigaword-50)(Rndm)(-blacklist)",
            "Familial Words & Common Names 1-Gram Counts",
            "Total Sentence Count",
            "Average Tokens Per Sentence",
            "Average Word Length",
            "Exclamation Marks Per Sentence",
            "Dashes Per Sentence",
            "Proportion Of Tokens That Are Stop Words",
            "Proportion Of Chars That Are Capitalized",
            "Topical Proximity - Fancy Science (glove-wiki-gigaword-50)",
            "Topical Proximity - Condenscension (glove-wiki-gigaword-50)",
            "Topical Proximity - Intoxication (glove-wiki-gigaword-50)",
            "Average Root Verb Embedding (glove-wiki-gigaword-50)",
        ],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=XGBClassifier,
        random_state=RANDOM_SEED,
        n_estimators=38,
        max_depth=4,
        min_child_weight=1,
        gamma=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_lambda=1,
        reg_alpha=0.1,
        learning_rate=0.01,
        objective="multi:softprob",
        num_class=5,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-twitter-25)(Rndm)",
            "Total Sentence Count",
            "Average Tokens Per Sentence",
            "Average Word Length",
            "Exclamation Marks Per Sentence",
            "Dashes Per Sentence",
            "Proportion Of Tokens That Are Stop Words",
            "Proportion Of Chars That Are Capitalized",
            "Previous Speaker",
        ],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=LogisticRegression,
        random_state=RANDOM_SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Total Sentence Count",
            "Average Tokens Per Sentence",
            "Average Word Length",
            "Exclamation Marks Per Sentence",
            "Question Marks Per Sentence",
            "Proportion Of Tokens That Are Stop Words",
            "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)(glove-twitter-50)(Rndm)",
            "Topical Proximity - Fancy Science (glove-wiki-gigaword-50)",
        ],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=LogisticRegression,
        penalty="l2",
        C=0.7,
        solver="saga",
        max_iter=1400,
        random_state=RANDOM_SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-50)(Rndm)",
            "Average Root Verb Embedding (fasttext-wiki-news-subwords-300)",
            "All 2-Gram One Hots",
            "Average Word Length",
            "Proportion Of Tokens That Are Stop Words",
            "Exclamation Marks Per Sentence",
            "Dashes Per Sentence",
        ],
        spacy_model_name="en_core_web_sm",
        use_by_episode_splits=False,
        model_type=GradientBoostingClassifier,
        n_estimators=45,
        learning_rate=0.2,
        max_depth=5,
        random_state=RANDOM_SEED,
    ),
]

FEATURE_EXTRACTORS.update(
    {
        "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-wiki-gigaword-50)(Rndm)(-blacklist)": partial(
            neighborhood_degrees_of_presence,
            gensim_model_slug="glove-wiki-gigaword-50",
            weight_decay_rate=0.5,
            n_neighbors=5,
            lemmatize=True,
            max_top_n=4,
            save_neighborhoods=True,
        )
    }
)

BEST_EXPERIMENT = ConfiguredExperiment(
    feature_extractor_names=[
        "Average Word Length",
        "Question Marks Per Sentence",
        "Exclamation Marks Per Sentence",
        "Dashes Per Sentence",
        "Familial Words & Common Names 1-Gram One Hots",
        "Hand-Selected POS-Tag N-Gram Counts",
        "Proportion Of Tokens That Are Stop Words",
        "Proportion Of Chars That Are Capitalized",
        "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-wiki-gigaword-50)(Rndm)(-blacklist)",
    ],
    spacy_model_name="en_core_web_sm",
    save_model=True,
    model_type=LogisticRegression,
    penalty="l2",
    C=1.94,
    solver="lbfgs",
    random_state=36,
    max_iter=1400,
)


GENERATED_EXPERIMENTS = generate_experiments(0)  # 1200

EXPERIMENTS = [BEST_EXPERIMENT]  # (
#     BASELINE_EXPERIMENTS + MANUALLY_CONFIGURED_EXPERIMENTS + GENERATED_EXPERIMENTS
# )
