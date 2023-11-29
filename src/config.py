from typing import Dict, List
from functools import partial

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
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
    avg_root_verb_embedding,
    avg_non_proper_noun_embedding,
    most_characteristic_n_gram_counts,
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
# - Augment data for underepresented classes
# - Have bigger dev & test sets
# - Add vader or other rule-based sentiment analysis?
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
    "Average Non-Proper Noun Embedding (glove-twitter-25)": partial(
        avg_non_proper_noun_embedding, gensim_model_slug="glove-twitter-25"
    ),
    # N-Gram One Hots
    "All 1-Gram One Hots": partial(all_n_gram_one_hots, n=1),
    "All 2-Gram One Hots": partial(all_n_gram_one_hots, n=2),
    "All 3-Gram One Hots": partial(all_n_gram_one_hots, n=3),
    # Most Characteristic N-Grams
    "400 Most Characteristic 1-Grams": partial(
        most_characteristic_n_gram_counts, num=200, n=1
    ),
    "200 Most Characteristic 2-Grams": partial(
        most_characteristic_n_gram_counts, num=90, n=2
    ),
    "100 Most Characteristic 3-Grams": partial(
        most_characteristic_n_gram_counts, num=15, n=3
    ),
    "5 Most Characteristic 4-Grams": partial(
        most_characteristic_n_gram_counts, num=5, n=4
    ),
    "1000 Most Characteristic 1-Grams": partial(
        most_characteristic_n_gram_counts, num=1000, n=1
    ),
    "700 Most Characteristic 2-Grams": partial(
        most_characteristic_n_gram_counts, num=700, n=2
    ),
    "500 Most Characteristic 3-Grams": partial(
        most_characteristic_n_gram_counts, num=500, n=3
    ),
    "100 Most Characteristic 4-Grams": partial(
        most_characteristic_n_gram_counts, num=100, n=4
    ),
    "70 Most Characteristic 1-Grams": partial(
        most_characteristic_n_gram_counts, num=70, n=1
    ),
    "50 Most Characteristic 2-Grams": partial(
        most_characteristic_n_gram_counts, num=50, n=2
    ),
    "30 Most Characteristic 3-Grams": partial(
        most_characteristic_n_gram_counts, num=30, n=3
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
    # Other
    "Proportion Of Tokens That Are Stop Words": proportion_stop_words,
    "Proportion Of Chars That Are Capitalized": proportion_alpha_chars_capitalized,
}


FEATURE_COMBOS_TO_TRY = [
    [
        "Total Sentence Count",  # Baseline 1
    ],
    [
        "All 1-Gram One Hots",  # Baseline 2
    ],
    [
        "Total Sentence Count",
        "Average Tokens Per Sentence",
        "Average Word Length",
        "Question Marks Per Sentence",
        "Exclamation Marks Per Sentence",
        "Dashes Per Sentence",
        "Proportion Of Tokens That Are Stop Words",
        "Proportion Of Chars That Are Capitalized",
        "Topical Proximity - Dubiety (glove-twitter-25)",
        "Topical Proximity - Death (glove-twitter-25)",
        "Topical Proximity - Sexual (glove-twitter-25)",
        "Topical Proximity - Condescension (glove-twitter-25)",
        "Topical Proximity - Intoxication (glove-twitter-25)",
        "Topical Proximity - Gratitude (glove-twitter-25)",
        "Topical Proximity - SciFi Creature (glove-twitter-25)",
        "Topical Proximity - Generic Emotion (glove-twitter-25)",
        "Topical Proximity - Fancy Science (glove-twitter-25)",
        "Topical Proximity - Food (glove-twitter-25)",
    ],
]


CONFIGURED_EXPERIMENTS: List[ConfiguredExperiment] = [
    # ConfiguredExperiment(
    #     feature_extractor_names=FEATURE_COMBOS_TO_TRY[1],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=LogisticRegression,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=FEATURE_COMBOS_TO_TRY[1],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=SVC,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=FEATURE_COMBOS_TO_TRY[1],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=GradientBoostingClassifier,
    #     max_depth=4,
    #     random_state=RANDOM_SEED,
    # ),
    # ConfiguredExperiment(
    #     feature_extractor_names=FEATURE_COMBOS_TO_TRY[1],
    #     spacy_model_name="en_core_web_sm",
    #     model_type=GaussianNB,
    # ),
    ConfiguredExperiment(
        feature_extractor_names=FEATURE_COMBOS_TO_TRY[2],
        spacy_model_name="en_core_web_sm",
        model_type=RickPredictor,
    )
]
