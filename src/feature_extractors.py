import json
import re
from collections import Counter
from typing import Dict, List, Optional, Set

import numpy as np
from spacy.tokens import Doc

from src.globals import (HAND_SELECTED_POS_BIGRAMS, HAND_SELECTED_POS_TRIGRAMS,
                         NEIGHBORHOODS_FPATH, RANDOM_SEED, TOKEN_BLACKLIST,
                         WORD_CLUSTERS)
from src.helpers import (convert_doc_to_n_grams, cosine_similarity,
                         get_exponentially_decaying_weights,
                         get_neighborhoods_from_training_data,
                         load_embedding_model)
from src.schema.feature_extractor import feature_extractor


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
def all_n_gram_one_hots(
    doc: Doc,
    n: int,
    lemmatize: bool = False,
    append_depedency_labels: bool = False,
    use_blacklist: bool = False,
    whitelist: Optional[Set[str]] = None,
) -> Dict[str, float]:
    """Extracts one-hot features for all n-grams in the input text."""
    n_grams = convert_doc_to_n_grams(
        doc, n, lemmatize=lemmatize, append_depedency_labels=append_depedency_labels
    )
    if whitelist is not None:  # Reduce to whitelist only
        n_grams = [ng for ng in n_grams if ng.lower() in whitelist]
    suffix = "_lem" if lemmatize else ""
    suffix += "_dep" if append_depedency_labels else ""
    if use_blacklist:
        feats = {f"has({ng}){suffix}": 1 for ng in n_grams if ng not in TOKEN_BLACKLIST}
        blacklisted = [f"has({ng})" for ng in n_grams if ng in TOKEN_BLACKLIST]
        if len(blacklisted) > 0:
            print(f"Blacklisted: {blacklisted}")
    else:
        feats = {f"has({ng}){suffix}": 1 for ng in n_grams}
    return feats


@feature_extractor
def all_n_gram_counts(
    doc: Doc,
    n: int,
    lemmatize: bool = False,
    append_depedency_labels: bool = False,
    normalize: bool = False,
    use_blacklist: bool = False,
    whitelist: Optional[Set[str]] = None,
) -> Dict[str, float]:
    """Extracts one-hot features for all n-grams in the input text."""
    n_grams = convert_doc_to_n_grams(
        doc, n, lemmatize=lemmatize, append_depedency_labels=append_depedency_labels
    )
    if whitelist is not None:  # Reduce to whitelist only
        n_grams = [ng for ng in n_grams if ng.lower() in whitelist]
    counts = Counter(n_grams)
    if normalize:
        counts = {n_gram: count / len(n_grams) for n_gram, count in counts.items()}
    suffix = "_lem" if lemmatize else ""
    suffix += "_dep" if append_depedency_labels else ""
    if use_blacklist:
        feats = {f"has({ng}){suffix}": 1 for ng in n_grams if ng not in TOKEN_BLACKLIST}
        blacklisted = [f"count({ng})" for ng in n_grams if ng in TOKEN_BLACKLIST]
        if len(blacklisted) > 0:
            print(f"Blacklisted: {blacklisted}")
    else:
        feats = {f"count({ng}){suffix}": count for ng, count in counts.items()}
    return feats


@feature_extractor
def proportion_alpha_chars_capitalized(doc: Doc) -> Dict[str, float]:
    """Extracts the percentage of alphabetic characters in the input text that are
    capitalized.
    """
    alpha_chars = [char for char in doc.text if char.isalpha()]
    n_capitalized = sum([char.isupper() for char in alpha_chars])
    return {"percent_alpha_chars_capitalized": n_capitalized / len(alpha_chars)}


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
def pos_tag_n_gram_counts(doc: Doc, n: int) -> Dict[str, float]:
    """Extracts the counts of POS tag n-gramgs in the input text."""
    pos_tags = [tok.pos_ for tok in doc]
    n_grams = []
    for start_idx in range(len(pos_tags) - n + 1):
        n_gram = " ".join(pos_tags[start_idx : start_idx + n])
        n_grams.append(n_gram)
    return {f"has('{ng}')": count for ng, count in Counter(n_grams).items()}


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


@feature_extractor
def neighborhood_degrees_of_presence(
    doc: Doc,
    gensim_model_slug: str,
    use_by_episode_split: bool = False,
    lemmatize: bool = True,
    max_top_n: Optional[int] = None,
    normalize: bool = False,
    weight_decay_rate: Optional[float] = None,
    n_neighbors: int = 5,
    use_blacklist: bool = False,
    neighborhoods: Optional[Dict[str, np.ndarray]] = None,
    save_neighborhoods: bool = False,
) -> Dict[str, float]:
    """See README.md for more info.""" ""
    suffix = "_norm" if lemmatize else ""
    suffix += "_lem" if normalize else ""
    if not neighborhoods:
        neighborhoods = get_neighborhoods_from_training_data(
            use_by_episode_split=use_by_episode_split,
            n_neighbors=n_neighbors,
            lemmatize=lemmatize,
            gensim_model_slug=gensim_model_slug,
        )
    if save_neighborhoods:
        serializable_neighborhoods = {
            w: np.round(nghbhd, 2).tolist() for w, nghbhd in neighborhoods.items()
        }
        with open(NEIGHBORHOODS_FPATH, "w") as f:
            json.dump(serializable_neighborhoods, f)
    model = load_embedding_model(gensim_model_slug)
    degrees_of_presence_by_neighborhood = {}
    for word, neighborhood in neighborhoods.items():
        if use_blacklist and word in TOKEN_BLACKLIST:
            continue
        feature_key = f"deg_of_presence({word}){suffix}"
        cos_similarities = []
        for token in doc:
            if token.is_stop or token.is_punct or token.is_space:
                continue
            try:
                token_embedding = model[token.text.lower()]
            except KeyError:
                continue
            cos_similarity = cosine_similarity(token_embedding, neighborhood)
            cos_similarities.append(cos_similarity)
        if len(cos_similarities) == 0:
            degrees_of_presence_by_neighborhood[feature_key] = 0.0
            continue
        highest_to_lowest_sims = sorted(cos_similarities, reverse=True)
        if max_top_n is None:  # Mimicking an unlimited number of counts
            filtered_high_to_low_similarities = highest_to_lowest_sims
        else:  # Mimicking a limited number of possible counts
            filtered_high_to_low_similarities = highest_to_lowest_sims[:max_top_n]
        if weight_decay_rate is None:
            weighted_similarities = filtered_high_to_low_similarities
        else:
            n_similarities = len(filtered_high_to_low_similarities)
            weights = get_exponentially_decaying_weights(
                n_weights=n_similarities,
                decay_rate=weight_decay_rate,
            )
            weighted_similarities = [
                sim * weight
                for sim, weight in zip(filtered_high_to_low_similarities, weights)
            ]
        deg_of_presence = sum(weighted_similarities)
        if normalize:
            deg_of_presence /= n_similarities
        degrees_of_presence_by_neighborhood[feature_key] = deg_of_presence
    return degrees_of_presence_by_neighborhood
