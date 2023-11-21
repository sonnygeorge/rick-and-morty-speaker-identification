from typing import Dict

from spacy.tokens import Doc

from src.schema.feature_extractor import feature_extractor


@feature_extractor
def get_avg_noun_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all nouns in the input text."""
    return {"noun_01": 1.0}  # FIXME


@feature_extractor
def get_avg_verb_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all verbs in the input text."""
    return {"verb_01": 1.0}  # FIXME
