from typing import Dict, List
from collections import Counter
import re

from spacy.tokens import Doc
import numpy as np

from src.schema.feature_extractor import feature_extractor
from src.helpers import (
    load_embedding_model,
    get_most_characteristic_n_grams_in_training_data,
    convert_text_to_n_grams,
)
from src.globals import (
    HAND_SELECTED_POS_BIGRAMS,
    HAND_SELECTED_POS_TRIGRAMS,
    WORD_CLUSTERS,
    RANDOM_SEED,
)


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
def avg_root_verb_embedding(doc: Doc, gensim_model_slug: str) -> Dict[str, float]:
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
        model = load_embedding_model(gensim_model_slug)
        root_verb_embeddings = []
        for verb in root_verbs:
            verb = re.sub(r"[^\w\s]", "", verb.lower())
            try:
                root_verb_embeddings.append(model[verb])
            except KeyError:
                print(f"🔍 Verb not in embedding model: {verb}")
        # Include feature for number of root verbs with found embeddings
        n_root_verbs_embedded = len(root_verb_embeddings)
        output["n_root_verbs_embedded"] = n_root_verbs_embedded
        if n_root_verbs_embedded > 0:
            avg_embedding = sum(root_verb_embeddings) / n_root_verbs
            for i, value in enumerate(avg_embedding):  # Add each dim as a feature
                output[f"avg_root_verb_embedding_{i}"] = value
    return output


@feature_extractor
def avg_non_proper_noun_embedding(doc: Doc, gensim_model_slug: str) -> Dict[str, float]:
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
        model = load_embedding_model(gensim_model_slug)
        non_proper_noun_embeddings = []
        for noun in non_proper_nouns:
            noun = re.sub(r"[^\w\s]", "", noun.lower())
            try:
                non_proper_noun_embeddings.append(model[noun])
            except KeyError:
                print(f"🔍 Noun not in embedding model: {noun}")
        # Include feature for number of non-proper nouns with found embeddings
        n_non_proper_nouns_embedded = len(non_proper_noun_embeddings)
        output["n_non_proper_nouns_embedded"] = n_non_proper_nouns_embedded
        if n_non_proper_nouns_embedded > 0:
            avg_embedding = sum(non_proper_noun_embeddings) / n_non_proper_nouns
            for i, value in enumerate(avg_embedding):
                output[f"avg_non_proper_noun_embedding_{i}"] = value
    print(output)
    return output


@feature_extractor
def most_characteristic_n_gram_counts(doc: Doc, num: int, n: int) -> Dict[str, float]:
    # TODO: Docstring
    characteristic_n_grams = get_most_characteristic_n_grams_in_training_data(num, n)
    doc_n_grams = convert_text_to_n_grams(doc.text, n)
    filtered_n_grams = [ng for ng in doc_n_grams if ng in characteristic_n_grams]
    return {f"'{ng}'": count for ng, count in Counter(filtered_n_grams).items()}


@feature_extractor
def pos_tag_n_gram_counts(doc: Doc, n: int) -> Dict[str, float]:
    """Extracts the counts of POS tag n-gramgs in the input text."""
    pos_tags = [tok.pos_ for tok in doc]
    n_grams = []
    for start_idx in range(len(pos_tags) - n + 1):
        n_gram = " ".join(pos_tags[start_idx : start_idx + n])
        n_grams.append(n_gram)
    return {f"'{ng}'": count for ng, count in Counter(n_grams).items()}


@feature_extractor
def get_counts_of_hand_selected_pos_n_grams(doc: Doc) -> Dict[str, float]:
    """Extracts the counts of certain, hand-selected POS tag n-grams in the input
    text.
    """
    pos_bigrams_counts = pos_tag_n_gram_counts(doc, n=2)
    pos_trigrams_counts = pos_tag_n_gram_counts(doc, n=3)
    hand_selected_counts = {}
    for bigram in HAND_SELECTED_POS_BIGRAMS:
        hand_selected_counts[bigram] = pos_bigrams_counts.get(bigram, 0)
    for trigram in HAND_SELECTED_POS_TRIGRAMS:
        hand_selected_counts[trigram] = pos_trigrams_counts.get(trigram, 0)
    return hand_selected_counts


@feature_extractor
def topical_proximity_score(
    doc: Doc, gensim_model_slug: str, topic_cluster: str
) -> Dict[str, float]:
    """Estimates a score for how close the input text is to a given topic cluster."""
    model = load_embedding_model(gensim_model_slug)
    topic_words = WORD_CLUSTERS[topic_cluster]
    topic_word_vecs = [model[word] for word in topic_words if word in model]
    np.random.seed(RANDOM_SEED)
    randomly_sampled_idxs = np.random.choice(
        len(topic_word_vecs),
        (5, int(len(topic_word_vecs) / 3)),
        replace=True,
    )
    centroids = []
    for sampled_idxs in randomly_sampled_idxs:
        vecs = [topic_word_vecs[idx] for idx in sampled_idxs]
        centroid = sum(vecs) / len(sampled_idxs)
        centroids.append(centroid)
    # Iterate and get a weighted similarity score of most similar words
    n_closest = 3
    weights = [1, 0.75, 0.2]
    top_similarities = []
    lowest_sim_in_top_similarities = 0
    for token in doc:
        if token.is_stop or token.is_punct or token.is_space:
            continue
        try:
            token_embedding = model[token.text]
        except KeyError:
            continue
        cos_similarities = [  # Between 0 and 1
            np.dot(token_embedding, centroid)
            / (np.linalg.norm(token_embedding) * np.linalg.norm(centroid))
            for centroid in centroids
        ]
        sim_to_most_similar_centroid = max(cos_similarities)
        if sim_to_most_similar_centroid > lowest_sim_in_top_similarities:
            top_similarities.append(sim_to_most_similar_centroid)
            top_similarities.sort(reverse=True)
            top_similarities = top_similarities[:n_closest]
            lowest_sim_in_top_similarities = top_similarities[-1]
    if len(top_similarities) == 0:
        weighted_similarity = 0
    else:
        weighted_similarity = sum(
            [sim * weight for sim, weight in zip(top_similarities, weights)]
        )
    topic_str = topic_cluster.lower().replace(" ", "_")
    return {f"topical_proximity_{topic_str}": weighted_similarity}
