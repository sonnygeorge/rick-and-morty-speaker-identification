from typing import Dict, List
from functools import partial

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from src.feature_extractors import (
    total_sentence_count,
    avg_tokens_per_sentence,
    avg_token_length,
    proportion_stop_words,
    proportion_alpha_chars_capitalized,
    question_marks_per_sentence,
    exclamation_marks_per_sentence,
    dashes_per_sentence,
    all_n_gram_counts,
    avg_root_verb_embedding,
    neighborhood_degrees_of_presence,
    all_n_gram_one_hots,
    pos_tag_n_gram_counts,
    get_counts_of_hand_selected_pos_n_grams,
    topical_proximity_score,
)
from src.schema.feature_extractor import FeatureExtractor
from src.schema.configured_experiment import ConfiguredExperiment
from src.helpers import RickPredictor
from src.globals import RANDOM_SEED

# TODO:
# - Add vader or other rule-based sentiment analysis?

# - Augment data for underepresented classes
# - Have bigger dev & test sets
# - Try to better normalize some features to length?
# - Write tests for feature extractors?


FEATURE_EXTRACTORS: Dict[str, FeatureExtractor] = {
    # "Length features"
    "Total Sentence Count": total_sentence_count,
    "Average Tokens Per Sentence": avg_tokens_per_sentence,
    "Average Word Length": avg_token_length,
    # Prevalance of different punctuation marks
    "Question Marks Per Sentence": question_marks_per_sentence,
    "Exclamation Marks Per Sentence": exclamation_marks_per_sentence,
    "Dashes Per Sentence": dashes_per_sentence,
    # Average word embeddings
    "Average Root Verb Embedding (glove-twitter-25)": partial(
        avg_root_verb_embedding, gensim_model_slug="glove-twitter-25"
    ),
    # N-Gram One Hots
    "All 1-Gram One Hots": partial(all_n_gram_one_hots, n=1),
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
    "All 1-Gram Counts": partial(all_n_gram_counts, n=1),
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
    # Topical Proximity Scores
    "Topical Proximity - Dubiety (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Dubiety",
    ),
    "Topical Proximity - Death (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Death",
    ),
    "Topical Proximity - Sexual (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Sexual",
    ),
    "Topical Proximity - Condescension (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Condescension",
    ),
    "Topical Proximity - Intoxication (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Intoxication",
    ),
    "Topical Proximity - Gratitude (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Gratitude",
    ),
    "Topical Proximity - SciFi Creature (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="SciFi Creature",
    ),
    "Topical Proximity - Generic Emotion (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Generic Emotion",
    ),
    "Topical Proximity - Fancy Science (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Fancy Science",
    ),
    "Topical Proximity - Food (glove-twitter-25)": partial(
        topical_proximity_score,
        gensim_model_slug="glove-twitter-25",
        topic_cluster="Food",
    ),
    # Neighborhood degrees of presence
    "Nghbhood Degrees - Lemmas (no-decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    "Nghbhood Degrees - Full Tokens (no-decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        gensim_model_slug="glove-twitter-25",
        lemmatize=False,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,4topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        max_top_n=4,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=False,
        n_neighbors=5,
        max_top_n=1,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=True,
        weight_decay_rate=0.5,
        n_neighbors=5,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=True,
        weight_decay_rate=0.5,
        max_top_n=4,
        n_neighbors=5,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-25)(Epsd)": partial(
        neighborhood_degrees_of_presence,
        use_by_episode_split=True,
        weight_decay_rate=0.5,
        max_top_n=1,
        n_neighbors=5,
        gensim_model_slug="glove-twitter-25",
        lemmatize=True,
    ),
    # Other
    "Proportion Of Tokens That Are Stop Words": proportion_stop_words,
    "Proportion Of Chars That Are Capitalized": proportion_alpha_chars_capitalized,
    # Previous speaker
    "Previous Speaker": None,
}


FEATURE_COMBOS_TO_TRY = [
    [  # Best yet w/ LogReg (acc = approx. .6)
        "All 1-Gram One Hots",
        "Total Sentence Count",
        "Average Tokens Per Sentence",
        "Average Word Length",
        "Exclamation Marks Per Sentence",
        "Dashes Per Sentence",
        "Proportion Of Tokens That Are Stop Words",
        "Proportion Of Chars That Are Capitalized",
        "Previous Speaker",
    ],
]


CONFIGURED_EXPERIMENTS: List[ConfiguredExperiment] = [
    # ConfiguredExperiment(
    #     feature_extractor_names=["All 1-Gram One Hots"],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=RickPredictor,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=["All 1-Gram One Hots"],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=LogisticRegression,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=[
    #         "Nghbhood Degrees - Lemmas (no-decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)"
    #     ],
    #     spacy_model_name="en_core_web_md",
    #     use_by_episode_splits=True,
    #     model_type=LogisticRegression,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=[
    #         "Nghbhood Degrees - Full Tokens (no-decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)"
    #     ],
    #     spacy_model_name="en_core_web_md",
    #     use_by_episode_splits=True,
    #     model_type=LogisticRegression,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=[
    #         "Nghbhood Degrees - Lemmas (no-decay,4topn,5nghbrs)(glove-twitter-25)(Epsd)"
    #     ],
    #     spacy_model_name="en_core_web_md",
    #     use_by_episode_splits=True,
    #     model_type=LogisticRegression,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=[
    #         "Nghbhood Degrees - Lemmas (no-decay,1topn,5nghbrs)(glove-twitter-25)(Epsd)"
    #     ],
    #     spacy_model_name="en_core_web_md",
    #     use_by_episode_splits=True,
    #     model_type=LogisticRegression,
    #     random_state=RANDOM_SEED,
    # ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,no-topn,5nghbrs)(glove-twitter-25)(Epsd)"
        ],
        spacy_model_name="en_core_web_md",
        use_by_episode_splits=True,
        model_type=LogisticRegression,
        random_state=RANDOM_SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,4topn,5nghbrs)(glove-twitter-25)(Epsd)"
        ],
        spacy_model_name="en_core_web_md",
        use_by_episode_splits=True,
        model_type=LogisticRegression,
        random_state=RANDOM_SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Nghbhood Degrees - Lemmas (.5decay,1topn,5nghbrs)(glove-twitter-25)(Epsd)"
        ],
        spacy_model_name="en_core_web_md",
        use_by_episode_splits=True,
        model_type=LogisticRegression,
        random_state=RANDOM_SEED,
    ),
]
