"""Text preparation utilities for the UN General Debate corpus."""

from __future__ import annotations

import re
from typing import Iterable

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize


DEFAULT_EXTRA_STOPWORDS = {
    "nation",
    "united",
    "organization",
    "assembly",
    "general",
    "would",
    "could",
    "may",
    "also",
}


def validate_columns(df: pd.DataFrame) -> None:
    """Raise a helpful error when required UNGD columns are missing."""
    required = {"country", "session", "year", "text"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def load_ungd(path: str) -> pd.DataFrame:
    """Load the UNGD CSV and perform basic schema validation."""
    df = pd.read_csv(path)
    validate_columns(df)
    return df


def clean_text(
    text: str,
    *,
    extra_stopwords: Iterable[str] | None = None,
    stem: bool = False,
) -> str:
    """Normalize one speech while preserving a transparent preprocessing chain.

    Steps are based on the original coursework notebook: lowercase text,
    remove punctuation/special characters, tokenize, remove English stopwords,
    and optionally apply Snowball stemming.
    """
    text = str(text).lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    stop_words.update(DEFAULT_EXTRA_STOPWORDS)
    if extra_stopwords:
        stop_words.update(extra_stopwords)

    tokens = [
        token
        for token in tokens
        if token not in stop_words and not token.isdigit() and len(token) > 2
    ]

    if stem:
        stemmer = SnowballStemmer("english")
        tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(tokens)


def add_text_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with basic reproducible text features."""
    validate_columns(df)
    out = df.copy()
    out["text"] = out["text"].fillna("").astype(str)
    out["text_length"] = out["text"].str.len()
    out["processed_text"] = out["text"].map(clean_text)
    return out
