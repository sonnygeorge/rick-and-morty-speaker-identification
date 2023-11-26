from typing import Dict, List
import re

from spacy.tokens import Doc
import gensim.downloader

from src.schema.feature_extractor import feature_extractor

EMBEDDING_MODEL = gensim.downloader.load("glove-twitter-25")  # FIXME: pass as arg


@feature_extractor
def total_sentence_count(doc: Doc) -> Dict[str, float]:
    """Extracts the total number of sentences in the input text."""
    return {"total_sentence_count": len(list(doc.sents))}


@feature_extractor
def avg_tokens_per_sentence(doc: Doc) -> Dict[str, float]:
    """Extracts the average number of tokens per sentence in the input text."""
    return {"avg_tokens_per_sentence": len(doc) / len(list(doc.sents))}


@feature_extractor
def avg_token_length(doc: Doc) -> Dict[str, float]:
    """Extracts the average number of characters per token in the input text."""
    return {"avg_token_length": sum([len(token) for token in doc]) / len(doc)}


@feature_extractor
def proportion_stop_words(doc: Doc) -> Dict[str, float]:
    """Extracts the proportion of tokens that are stop words in the input text."""
    return {"proportion_stop_words": sum([token.is_stop for token in doc]) / len(doc)}


@feature_extractor
def question_marks_per_sentence(doc: Doc) -> Dict[str, float]:
    """Extracts the average number of question marks per sentence in the input text."""
    n_question_marks = sum(["?" in token.text for token in doc])
    return {"question_marks_per_sentence": n_question_marks / len(list(doc.sents))}


@feature_extractor
def exclamation_marks_per_sentence(doc: Doc) -> Dict[str, float]:
    """Extracts the average number of exclamation marks per sentence in the input text."""
    n_exclamations = sum(["!" in token.text for token in doc])
    return {"exclamation_marks_per_sentence": n_exclamations / len(list(doc.sents))}


@feature_extractor
def dashes_per_sentence(doc: Doc) -> Dict[str, float]:
    """Extracts the average number of dashes per sentence in the input text."""
    n_dashes = sum(["-" in token.text for token in doc])
    return {"dashes_per_sentence": n_dashes / len(list(doc.sents))}


@feature_extractor
def avg_root_verb_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all root verbs in the input text."""
    # Find all root verbs
    root_verbs: List[str] = []
    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            root_verbs.append(token.text)
    # Include feature for number of root verbs found
    n_root_verbs = len(root_verbs)
    output = {"n_root_verbs": n_root_verbs}
    # If there are root verbs, proceed to get embeddings
    if n_root_verbs > 0:
        root_verb_embeddings = []
        for verb in root_verbs:
            verb = re.sub(r"[^\w\s]", "", verb.lower())
            try:
                root_verb_embeddings.append(EMBEDDING_MODEL[verb])
            except KeyError:
                print(f"Verb not in embedding model: {verb}")
        # Include feature for number of root verbs with found embeddings
        n_root_verbs_embedded = len(root_verb_embeddings)
        output["n_root_verbs_embedded"] = n_root_verbs_embedded
        if n_root_verbs_embedded > 0:
            avg_embedding = sum(root_verb_embeddings) / n_root_verbs
            for i, value in enumerate(avg_embedding):  # Add each dim as a feature
                output[f"avg_root_verb_embedding_{i}"] = value
    return output


@feature_extractor
def avg_non_proper_noun_embedding(doc: Doc) -> Dict[str, float]:
    """Extracts the average embedding of all non-proper nouns in the input text."""
    # Find all non-proper nouns (including compound nouns)
    non_proper_nouns: List[str] = []
    for token in doc:
        if token.pos_ == "NOUN" and not token.is_oov and not token.is_stop:
            non_proper_nouns.append(token.text)
    # Include feature for number of non-proper nouns found
    n_non_proper_nouns = len(non_proper_nouns)
    output = {"n_non_proper_nouns": n_non_proper_nouns}
    # If there are non-proper nouns, proceed to get embeddings
    if n_non_proper_nouns > 0:
        non_proper_noun_embeddings = []
        for noun in non_proper_nouns:
            noun = re.sub(r"[^\w\s]", "", noun.lower())
            try:
                non_proper_noun_embeddings.append(EMBEDDING_MODEL[noun])
            except KeyError:
                print(f"Noun not in embedding model: {noun}")
        # Include feature for number of non-proper nouns with found embeddings
        n_non_proper_nouns_embedded = len(non_proper_noun_embeddings)
        output["n_non_proper_nouns_embedded"] = n_non_proper_nouns_embedded
        if n_non_proper_nouns_embedded > 0:
            avg_embedding = sum(non_proper_noun_embeddings) / n_non_proper_nouns
            for i, value in enumerate(avg_embedding):
                output[f"avg_non_proper_noun_embedding_{i}"] = value
    return output


@feature_extractor
def avg_adjective_embedding(doc: Doc) -> Dict[str, float]:
    pass


@feature_extractor
def avg_adverb_embedding(doc: Doc) -> Dict[str, float]:
    pass
