"""Reusable topic-model estimators adapted from the original coursework."""

from __future__ import annotations

from dataclasses import dataclass

from gensim import corpora
from gensim.models import CoherenceModel, LdaModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer


@dataclass
class LDAResult:
    model: LdaModel
    corpus: list
    dictionary: corpora.Dictionary
    texts: list[list[str]]
    coherence: float


@dataclass
class NMFResult:
    model: NMF
    vectorizer: TfidfVectorizer
    document_topic_matrix: object
    topics: list[list[str]]
    coherence: float


def tokenize_for_coherence(documents: list[str]) -> list[list[str]]:
    """Tokenize documents once so model coherence is evaluated consistently."""
    stop_words = set(stopwords.words("english"))
    return [
        [
            word
            for word in simple_preprocess(str(doc))
            if word not in stop_words and not word.isdigit() and len(word) > 3
        ]
        for doc in documents
    ]


def topic_coherence(topics: list[list[str]], tokenized_docs: list[list[str]]) -> float:
    """Compute c_v coherence against a common tokenized reference corpus."""
    dictionary = corpora.Dictionary(tokenized_docs)
    model = CoherenceModel(
        topics=topics,
        texts=tokenized_docs,
        dictionary=dictionary,
        coherence="c_v",
    )
    return float(model.get_coherence())


def fit_lda(
    documents: list[str],
    *,
    num_topics: int = 10,
    no_above: float = 0.30,
    no_below: int = 10,
    passes: int = 50,
    random_state: int = 0,
) -> LDAResult:
    """Fit the LDA specification used in the original Africa analysis."""
    texts = tokenize_for_coherence(documents)
    dictionary = corpora.Dictionary(texts)
    dictionary.filter_extremes(no_above=no_above, no_below=no_below)
    corpus = [dictionary.doc2bow(text) for text in texts]

    model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=passes,
        random_state=random_state,
    )

    coherence = CoherenceModel(
        model=model,
        texts=texts,
        dictionary=dictionary,
        coherence="c_v",
    ).get_coherence()

    return LDAResult(model, corpus, dictionary, texts, float(coherence))


def lda_topic_prevalence(result: LDAResult) -> list[float]:
    """Return mean document-level probability for each LDA topic."""
    distributions = [
        dict(result.model.get_document_topics(bow, minimum_probability=0.0))
        for bow in result.corpus
    ]
    return [
        sum(doc.get(topic_id, 0.0) for doc in distributions) / len(distributions)
        for topic_id in range(result.model.num_topics)
    ]


def fit_nmf(
    documents: list[str],
    *,
    num_topics: int = 10,
    max_df: float = 0.95,
    min_df: int = 2,
    random_state: int = 0,
    top_n: int = 10,
) -> NMFResult:
    """Fit NMF to TF-IDF and evaluate topics against the same reference corpus."""
    vectorizer = TfidfVectorizer(
        max_df=max_df,
        min_df=min_df,
        stop_words="english",
    )
    tfidf = vectorizer.fit_transform(documents)
    model = NMF(n_components=num_topics, random_state=random_state)
    document_topic_matrix = model.fit_transform(tfidf)

    features = vectorizer.get_feature_names_out()
    topics = [
        [features[i] for i in topic.argsort()[:-top_n - 1:-1]]
        for topic in model.components_
    ]
    tokens = tokenize_for_coherence(documents)
    coherence = topic_coherence(topics, tokens)

    return NMFResult(model, vectorizer, document_topic_matrix, topics, coherence)


def fit_bertopic(
    documents: list[str],
    *,
    n_gram_range: tuple[int, int] = (1, 3),
    min_topic_size: int = 10,
    verbose: bool = False,
):
    """Fit BERTopic lazily so classical models do not require its dependencies."""
    from bertopic import BERTopic

    model = BERTopic(
        n_gram_range=n_gram_range,
        min_topic_size=min_topic_size,
        verbose=verbose,
    )
    topics, probabilities = model.fit_transform(documents)
    return model, topics, probabilities


def bertopic_word_lists(model, top_n: int = 10) -> list[list[str]]:
    """Return BERTopic topic words, excluding the outlier topic (-1)."""
    topic_ids = [topic_id for topic_id in model.get_topics() if topic_id != -1]
    return [
        [word for word, _ in model.get_topic(topic_id)[:top_n]]
        for topic_id in sorted(topic_ids)
    ]
