from typing import Dict, List

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from src.feature_extractors import (
    total_sentence_count,
    avg_tokens_per_sentence,
    avg_token_length,
    proportion_stop_words,
    question_marks_per_sentence,
    exclamation_marks_per_sentence,
    dashes_per_sentence,
    avg_root_verb_embedding,
    avg_non_proper_noun_embedding,
    avg_adjective_embedding,
    avg_adverb_embedding,
)
from src.schema.feature_extractor import FeatureExtractor
from src.schema.configured_experiment import ConfiguredExperiment
from src.globals import SEED


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
    "Average Root Verb Embedding": avg_root_verb_embedding,
    "Average Non-Proper Noun Embedding": avg_non_proper_noun_embedding,
    "Average Adjective Embedding": avg_adjective_embedding,
    "Average Adverb Embedding": avg_adverb_embedding,
    # Other
    "Porportion Of Tokens That Are Stop Words": proportion_stop_words,
}


CONFIGURED_EXPERIMENTS: List[ConfiguredExperiment] = [
    ConfiguredExperiment(
        feature_extractor_names=["Total Sentence Count"],
        spacy_model_name="en_core_web_sm",
        model_type=DecisionTreeClassifier,
        criterion="entropy",
        max_depth=5,
        random_state=SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Total Sentence Count",
            "Average Tokens Per Sentence",
            "Average Word Length",
            "Question Marks Per Sentence",
            "Exclamation Marks Per Sentence",
            "Dashes Per Sentence",
            "Average Root Verb Embedding",
            "Porportion Of Tokens That Are Stop Words",
        ],
        spacy_model_name="en_core_web_sm",
        model_type=GradientBoostingClassifier,
        random_state=SEED,
    ),
    ConfiguredExperiment(
        feature_extractor_names=[
            "Total Sentence Count",
            "Average Tokens Per Sentence",
            "Average Word Length",
            "Question Marks Per Sentence",
            "Exclamation Marks Per Sentence",
            "Dashes Per Sentence",
            "Average Root Verb Embedding",
            "Average Non-Proper Noun Embedding",
            "Porportion Of Tokens That Are Stop Words",
        ],
        spacy_model_name="en_core_web_sm",
        model_type=GradientBoostingClassifier,
        random_state=SEED,
    ),
]
