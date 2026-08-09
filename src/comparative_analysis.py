"""Reusable methods from the original Africa-Europe AI coursework.

The functions preserve the analytical ideas and key hyperparameters of the
submitted notebook while removing Google Colab paths and notebook side effects.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from gensim import corpora
from gensim.models import LdaModel
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class SimilarityResult:
    similarity: float
    vectorizer: TfidfVectorizer


@dataclass
class KMeansResult:
    model: KMeans
    vectorizer: TfidfVectorizer
    labels: np.ndarray


def corpus_cosine_similarity(
    africa_documents: list[str],
    europe_documents: list[str],
    *,
    max_features: int | None = None,
) -> SimilarityResult:
    """Compute TF-IDF cosine similarity between two regional corpora.

    Each regional corpus is concatenated into one document, matching the
    high-level comparison in the AI-course submission.
    """
    regional_docs = [
        " ".join(map(str, africa_documents)),
        " ".join(map(str, europe_documents)),
    ]
    vectorizer = TfidfVectorizer(max_features=max_features)
    matrix = vectorizer.fit_transform(regional_docs)
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0, 0])
    return SimilarityResult(similarity, vectorizer)


def fit_joint_lda(
    tokenized_documents: list[list[str]],
    *,
    num_topics: int = 10,
    no_above: float = 0.30,
    no_below: int = 10,
    passes: int = 50,
    random_state: int = 0,
) -> tuple[LdaModel, list, corpora.Dictionary]:
    """Fit the joint LDA specification used for Africa-Europe comparison."""
    dictionary = corpora.Dictionary(tokenized_documents)
    dictionary.filter_extremes(no_above=no_above, no_below=no_below)
    corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_documents]
    model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes,
        random_state=random_state,
    )
    return model, corpus, dictionary


def fit_kmeans_tfidf(
    documents: list[str],
    *,
    n_clusters: int = 3,
    random_state: int = 42,
    max_features: int | None = None,
) -> KMeansResult:
    """Fit K-means to TF-IDF features using the submitted three-cluster choice."""
    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    labels = model.fit_predict(matrix)
    return KMeansResult(model, vectorizer, labels)


def build_lstm_classifier(
    *,
    vocab_size: int = 10_000,
    sequence_length: int = 100,
    embedding_dim: int = 100,
    lstm_units: int = 128,
    num_classes: int = 2,
    learning_rate: float = 0.001,
):
    """Build the Keras LSTM architecture documented in the AI submission.

    TensorFlow is imported lazily because it is optional for users interested
    only in the classical NLP components.
    """
    try:
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense, Embedding, LSTM
        from tensorflow.keras.optimizers import Adam
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ImportError(
            "TensorFlow is required for the LSTM extension. "
            "Install requirements-ai.txt."
        ) from exc

    model = Sequential(
        [
            Embedding(vocab_size, embedding_dim, input_length=sequence_length),
            LSTM(lstm_units),
            Dense(num_classes, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model
