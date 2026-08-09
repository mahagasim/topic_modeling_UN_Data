"""Sentence-level VADER sentiment utilities for UN General Debate speeches."""

from __future__ import annotations

import re

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def split_sentences(text: str) -> list[str]:
    """Split a speech into non-empty sentence-like units.

    The original coursework applied sentence tokenization after the speech had
    already been reduced to individual tokens. This rebuild scores sentence
    units from the original speech text instead.
    """
    return [part.strip() for part in _SENTENCE_SPLIT.split(str(text)) if part.strip()]


def mean_vader_compound(text: str, analyzer: SentimentIntensityAnalyzer | None = None) -> float:
    """Return the mean VADER compound score across sentences in one speech."""
    analyzer = analyzer or SentimentIntensityAnalyzer()
    sentences = split_sentences(text)
    if not sentences:
        return 0.0
    scores = [analyzer.polarity_scores(sentence)["compound"] for sentence in sentences]
    return float(sum(scores) / len(scores))


def classify_sentiment(score: float, threshold: float = 0.05) -> str:
    """Classify a VADER compound score using conventional ±threshold cutoffs."""
    if score >= threshold:
        return "positive"
    if score <= -threshold:
        return "negative"
    return "neutral"


def add_sentiment_features(df: pd.DataFrame, text_column: str = "text") -> pd.DataFrame:
    """Return a copy with speech-level VADER score and sentiment category."""
    if text_column not in df.columns:
        raise ValueError(f"Missing text column: {text_column}")

    analyzer = SentimentIntensityAnalyzer()
    out = df.copy()
    out["sentiment_compound"] = out[text_column].fillna("").map(
        lambda value: mean_vader_compound(value, analyzer)
    )
    out["sentiment_label"] = out["sentiment_compound"].map(classify_sentiment)
    return out
