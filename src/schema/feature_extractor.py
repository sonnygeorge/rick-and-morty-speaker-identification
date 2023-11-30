from typing import Protocol, Any, Dict, Optional
from functools import wraps

import pandas as pd
from spacy.tokens import Doc


class FeatureExtractor(Protocol):
    """Defines a contract for feature extractors that process SpaCy Doc objects.

    A feature extractor is a callable that either:
    - Extracts features from a single SpaCy Doc object, or;
    - Takes and index values and a pd.Series of SpaCy Doc objects, and extracts
        features from the Doc at the given index.

    This flexibility is useful for caching strategies, where the extractor can be
    partially applied to a pd.Series of SpaCy Doc objects. The functions whose remaining
    argument, `index`, is serializable, is then wrapped in the caching layer.

    Args:
        doc (Optional[Doc]): A SpaCy Doc object.
        index (Optional[int]): Index in a pd.Series of SpaCy Doc objects.
        docs (Optional[pd.Series[Doc]]): A pd.Series of SpaCy Doc objects.
        **kwargs (Any): Additional keyword arguments.

    Returns:
        Dict[str, float]: Dictionary mapping feature names to their values.
    """

    def __call__(
        self,
        doc: Optional[Doc] = None,
        index: Optional[int] = None,
        docs: "Optional[pd.Series[Doc]]" = None,
        **kwargs: Any,  # Other arguments for the feature extractor
    ) -> Dict[str, float]:
        ...


class FeatureExtractorWithDocArgOnly(Protocol):
    """A simplified protocol for feature extraction functions that do not take `index`,
    or `docs` as arguments.

    This protocol is intended for basic feature extractors that operate solely on a
    single SpaCy Doc object, without the need for additional context or parameters.

    Args:
        doc (Optional[Doc]): A SpaCy Doc object.
        **kwargs (Any): Other arguments for the feature extractor.

    Returns:
        Dict[str, float]: Dictionary mapping feature names to their values.
    """

    def __call__(
        self,
        doc: Optional[Doc] = None,
        **kwargs: Any,  # Other arguments for the feature extractor
    ) -> Dict[str, float]:
        ...


# class CachableFeatureExtractor(Protocol):
#     """A protocol for feature extractors that have serializable arguments.

#     This protocol is intended for feature extractors that can be cached in memory: those
#     that have already had their `docs` argument partially applied, leaving only the
#     serializable `index` argument.

#     Args:
#         index (Optional[int]): Index in a pd.Series of SpaCy Doc objects.

#     Returns:
#         Dict[str, float]: Dictionary mapping feature names to their values.
#     """

#     def __call__(
#         self,
#         index: Optional[int] = None,
#         # **kwargs: Any NOTE: These should have already been partially applied
#     ) -> Dict[str, float]:
#         ...


def feature_extractor(func: FeatureExtractorWithDocArgOnly) -> FeatureExtractor:
    """Decorator that adapts a FeatureExtractorWithDocArgOnly function to conform to
    the FeatureExtractor protocol.

    This decorator enhances a basic feature extractor by adding the ability to handle
    additional arguments (`index`, and `docs`). This is useful for integrating simple
    extractors into systems that require these additional parameters, such as caching
    mechanisms.

    Returns:
        FeatureExtractor: A function adhering to the FeatureExtractor protocol.
    """

    @wraps(func)
    def wrapper(
        doc: Optional[Doc] = None,
        index: Optional[int] = None,
        docs: "Optional[pd.Series[Doc]]" = None,
        **kwargs: Any,
    ) -> Dict[str, float]:
        if docs is not None and index is not None:
            doc = docs[index]
            return func(doc, **kwargs)
        elif doc is not None:
            return func(doc, **kwargs)
        # Else raise an error
        raise ValueError("Must take either `doc` or `index` and `docs`")

    return wrapper
