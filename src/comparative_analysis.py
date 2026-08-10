"""Reusable methods for the Africa-Europe AI coursework and QA rebuild."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from gensim import corpora
from gensim.models import LdaModel
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split


@dataclass
class SimilarityResult:
    similarity: float
    vectorizer: TfidfVectorizer


@dataclass
class SimilaritySummary:
    """Three distinct TF-IDF similarity estimands.

    ``coursework_first_pair`` reproduces the original notebook's
    ``cosine_sim[0][0]`` implementation. It is one Europe-Africa speech pair,
    not a corpus-level statistic. ``centroid_cosine`` compares the two regional
    mean TF-IDF vectors. ``sampled_pairwise_mean`` averages a deterministic
    sample of cross-region speech-pair similarities.
    """

    coursework_first_pair: float
    centroid_cosine: float
    sampled_pairwise_mean: float
    pair_sample_size: int
    vectorizer: TfidfVectorizer


@dataclass
class KMeansResult:
    model: KMeans
    vectorizer: TfidfVectorizer
    labels: np.ndarray
    matrix: object


@dataclass
class LSTMData:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    tokenizer: object
    label_mapping: dict[str, int]


def corpus_cosine_similarity(
    africa_documents: list[str],
    europe_documents: list[str],
    *,
    max_features: int | None = None,
) -> SimilarityResult:
    """Compare two concatenated regional corpora with TF-IDF cosine similarity.

    This is an aggregate *professional* summary and is intentionally distinct
    from the coursework-reported 0.2640, which came from one speech pair.
    """
    if not africa_documents or not europe_documents:
        raise ValueError("Both regional document collections must be non-empty.")
    regional_docs = [
        " ".join(map(str, africa_documents)),
        " ".join(map(str, europe_documents)),
    ]
    vectorizer = TfidfVectorizer(max_features=max_features)
    matrix = vectorizer.fit_transform(regional_docs)
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0, 0])
    return SimilarityResult(similarity, vectorizer)


def cross_region_similarity_summary(
    documents: list[str],
    groups: list[str],
    *,
    group_a: str = "Africa",
    group_b: str = "Europe",
    pair_sample_size: int = 300,
    random_state: int = 42,
    max_features: int | None = None,
) -> SimilaritySummary:
    """Return clearly defined speech-pair and aggregate TF-IDF similarities."""
    if len(documents) != len(groups):
        raise ValueError("documents and groups must have the same length.")
    docs = np.asarray([str(d) for d in documents], dtype=object)
    labels = np.asarray(groups, dtype=object)
    mask_a = labels == group_a
    mask_b = labels == group_b
    if not mask_a.any() or not mask_b.any():
        raise ValueError(f"Both {group_a!r} and {group_b!r} must be present.")

    vectorizer = TfidfVectorizer(max_features=max_features)
    matrix = vectorizer.fit_transform(docs)
    A, B = matrix[mask_a], matrix[mask_b]

    # Original notebook used cosine_sim = cosine_similarity(Europe, Africa)
    # and printed cosine_sim[0][0]. Cosine is symmetric, so A/B order is
    # immaterial for the scalar value.
    first_pair = float(cosine_similarity(B[0], A[0])[0, 0])
    centroid = float(cosine_similarity(np.asarray(A.mean(axis=0)), np.asarray(B.mean(axis=0)))[0, 0])

    n = min(pair_sample_size, A.shape[0], B.shape[0])
    rng = np.random.default_rng(random_state)
    ia = rng.choice(A.shape[0], n, replace=False)
    ib = rng.choice(B.shape[0], n, replace=False)
    sampled_mean = float(cosine_similarity(A[ia], B[ib]).mean())

    return SimilaritySummary(first_pair, centroid, sampled_mean, n, vectorizer)


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
    if not tokenized_documents:
        raise ValueError("tokenized_documents must be non-empty.")
    dictionary = corpora.Dictionary(tokenized_documents)
    dictionary.filter_extremes(no_above=no_above, no_below=no_below)
    if len(dictionary) == 0:
        raise ValueError("Vocabulary is empty after filtering; relax no_above/no_below.")
    corpus = [dictionary.doc2bow(tokens) for tokens in tokenized_documents]
    model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes,
        random_state=random_state,
    )
    return model, corpus, dictionary


def lda_prevalence_by_group(model: LdaModel, corpus: list, groups: list[str]) -> pd.DataFrame:
    """Average document-level LDA topic probabilities within each group."""
    if len(corpus) != len(groups):
        raise ValueError("corpus and groups must have the same length.")
    rows = []
    for group in pd.unique(pd.Series(groups)):
        idx = [i for i, g in enumerate(groups) if g == group]
        if not idx:
            continue
        distributions = [
            dict(model.get_document_topics(corpus[i], minimum_probability=0.0))
            for i in idx
        ]
        for topic in range(model.num_topics):
            rows.append(
                {
                    "group": group,
                    "topic": topic,
                    "mean_probability": float(np.mean([d.get(topic, 0.0) for d in distributions])),
                }
            )
    return pd.DataFrame(rows)


def kmeans_elbow(
    documents: list[str],
    *,
    k_values: range | list[int] = range(1, 10),
    random_state: int = 42,
    max_features: int | None = None,
) -> pd.DataFrame:
    """Return inertia for a reproducible K-means elbow diagnostic."""
    if not documents:
        raise ValueError("documents must be non-empty.")
    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    rows = []
    for k in k_values:
        model = KMeans(n_clusters=int(k), random_state=random_state, n_init="auto")
        model.fit(matrix)
        rows.append({"k": int(k), "inertia": float(model.inertia_)})
    return pd.DataFrame(rows)


def fit_kmeans_tfidf(
    documents: list[str],
    *,
    n_clusters: int = 3,
    random_state: int = 42,
    max_features: int | None = None,
) -> KMeansResult:
    """Fit K-means to TF-IDF features using the submitted three-cluster choice."""
    if not documents:
        raise ValueError("documents must be non-empty.")
    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    matrix = vectorizer.fit_transform(documents)
    model = KMeans(n_clusters=n_clusters, random_state=random_state, n_init="auto")
    labels = model.fit_predict(matrix)
    return KMeansResult(model, vectorizer, labels, matrix)


def top_terms_per_cluster(result: KMeansResult, *, top_n: int = 10) -> pd.DataFrame:
    """Return the highest-centroid TF-IDF terms for each K-means cluster."""
    terms = result.vectorizer.get_feature_names_out()
    rows = []
    for cluster_id, center in enumerate(result.model.cluster_centers_):
        idx = center.argsort()[::-1][:top_n]
        rows.append({"cluster": cluster_id, "top_terms": ", ".join(terms[idx])})
    return pd.DataFrame(rows)


def build_lstm_classifier(
    *,
    vocab_size: int = 10_000,
    sequence_length: int = 100,
    embedding_dim: int = 100,
    lstm_units: int = 128,
    num_classes: int = 2,
    learning_rate: float = 0.001,
):
    """Build a modern Keras version of the submitted LSTM architecture."""
    try:
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import Dense, Embedding, Input, LSTM
        from tensorflow.keras.optimizers import Adam
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise ImportError(
            "TensorFlow is required for the LSTM extension. "
            "Install with `pip install -r requirements-ai.txt`."
        ) from exc

    model = Sequential(
        [
            Input(shape=(sequence_length,)),
            Embedding(vocab_size, embedding_dim),
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


def prepare_lstm_data(
    documents: list[str],
    labels: list[str],
    *,
    vocab_size: int = 10_000,
    sequence_length: int = 100,
    test_size: float = 0.20,
    random_state: int = 42,
) -> LSTMData:
    """Tokenize/pad text and create a held-out test split for LSTM analysis."""
    try:
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        from tensorflow.keras.preprocessing.text import Tokenizer
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "TensorFlow is required for the LSTM extension. "
            "Install with `pip install -r requirements-ai.txt`."
        ) from exc

    if len(documents) != len(labels):
        raise ValueError("documents and labels must have the same length.")
    unique = set(labels)
    if unique == {"Africa", "Europe"}:
        mapping = {"Europe": 0, "Africa": 1}
    else:
        mapping = {label: i for i, label in enumerate(sorted(unique))}
    y = np.asarray([mapping[label] for label in labels], dtype=np.int64)

    tokenizer = Tokenizer(num_words=vocab_size)
    tokenizer.fit_on_texts(documents)
    sequences = tokenizer.texts_to_sequences(documents)
    X = pad_sequences(sequences, maxlen=sequence_length)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return LSTMData(X_train, X_test, y_train, y_test, tokenizer, mapping)


def train_lstm_classifier(
    data: LSTMData,
    *,
    vocab_size: int = 10_000,
    sequence_length: int = 100,
    embedding_dim: int = 100,
    lstm_units: int = 128,
    learning_rate: float = 0.001,
    batch_size: int = 20,
    epochs: int = 10,
    validation_split: float = 0.15,
    verbose: int = 1,
):
    """Train/evaluate the LSTM without using the test set as validation data.

    The original coursework used the held-out test set as ``validation_data``
    during training. This helper keeps a separate validation slice of the
    training data and evaluates the test set only after fitting.
    """
    model = build_lstm_classifier(
        vocab_size=vocab_size,
        sequence_length=sequence_length,
        embedding_dim=embedding_dim,
        lstm_units=lstm_units,
        learning_rate=learning_rate,
    )
    history = model.fit(
        data.X_train,
        data.y_train,
        validation_split=validation_split,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
    )
    loss, accuracy = model.evaluate(data.X_test, data.y_test, verbose=0)
    pred = model.predict(data.X_test, verbose=0).argmax(axis=1)
    return {
        "model": model,
        "history": history,
        "test_loss": float(loss),
        "test_accuracy": float(accuracy),
        "confusion_matrix": confusion_matrix(data.y_test, pred),
        "classification_report": classification_report(data.y_test, pred, output_dict=True),
    }
