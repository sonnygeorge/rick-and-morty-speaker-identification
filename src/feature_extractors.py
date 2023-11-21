from typing import Dict

from spacy.tokens import Doc

from src.feature_extractor import feature_extractor


@feature_extractor
def get_avg_noun_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all nouns in the input text."""
    pass


@feature_extractor
def get_avg_verb_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all verbs in the input text."""
    pass
