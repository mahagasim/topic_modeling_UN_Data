"""Text preparation utilities for the UN General Debate corpus."""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


# Country-code sets reproduce the continent choices made in the original
# coursework mapping. In particular, Turkey was classified under Asia and is
# therefore not included in the Europe sample.
AFRICAN_COUNTRY_CODES = {
    "AGO", "BDI", "BEN", "BFA", "BWA", "CAF", "CIV", "CMR", "COD", "COG",
    "COM", "CPV", "DJI", "DZA", "EGY", "ERI", "ETH", "GAB", "GHA", "GIN",
    "GMB", "GNB", "GNQ", "KEN", "LBR", "LBY", "LSO", "MAR", "MDG", "MLI",
    "MOZ", "MRT", "MUS", "MWI", "NAM", "NER", "NGA", "RWA", "SDN", "SEN",
    "SLE", "SOM", "SSD", "STP", "SWZ", "SYC", "TCD", "TGO", "TUN", "TZA",
    "UGA", "ZAF", "ZMB", "ZWE",
}

EUROPEAN_COUNTRY_CODES = {
    "ALB", "AND", "AUT", "BEL", "BGR", "BIH", "BLR", "CHE", "CSK", "CYP",
    "CZE", "DDR", "DEU", "DNK", "ESP", "EST", "EU", "FIN", "FRA", "GBR",
    "GRC", "HRV", "HUN", "IRL", "ISL", "ITA", "LIE", "LTU", "LUX", "LVA",
    "MCO", "MDA", "MKD", "MLT", "MNE", "NLD", "NOR", "POL", "PRT", "ROU",
    "RUS", "SMR", "SVK", "SVN", "SWE", "UKR", "VAT", "YUG",
}

DEFAULT_EXTRA_STOPWORDS = {
    "nation", "nations", "united", "organization", "assembly", "general",
    "would", "could", "may", "also",
}


def validate_columns(df: pd.DataFrame) -> None:
    """Raise a helpful error when required UNGD columns are missing."""
    required = {"country", "session", "year", "text"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def load_ungd(path: str) -> pd.DataFrame:
    """Load the UNGD CSV and validate the core schema."""
    df = pd.read_csv(path)
    validate_columns(df)
    return df


def add_coursework_continent(df: pd.DataFrame) -> pd.DataFrame:
    """Add Africa/Europe labels using the continent mapping from the coursework.

    Countries outside the two focal regions receive ``None`` because the
    professional comparative notebook only needs the Africa-Europe subset.
    """
    validate_columns(df)
    out = df.copy()
    out["Continent"] = None
    out.loc[out["country"].isin(AFRICAN_COUNTRY_CODES), "Continent"] = "Africa"
    out.loc[out["country"].isin(EUROPEAN_COUNTRY_CODES), "Continent"] = "Europe"
    return out


def filter_africa(df: pd.DataFrame) -> pd.DataFrame:
    """Return speeches from the 54 African country codes present in the coursework."""
    validate_columns(df)
    return df.loc[df["country"].isin(AFRICAN_COUNTRY_CODES)].copy()


def filter_africa_europe(df: pd.DataFrame) -> pd.DataFrame:
    """Return the Africa-Europe comparison sample used by the AI coursework."""
    out = add_coursework_continent(df)
    return out.loc[out["Continent"].notna()].copy()


def clean_text(
    text: str,
    *,
    extra_stopwords: Iterable[str] | None = None,
    lemmatize: bool = True,
    stem: bool = False,
) -> str:
    """Normalize one speech with a transparent, configurable pipeline.

    The rebuild keeps the core logic of the original coursework while removing
    notebook-specific side effects and hard-coded paths.
    """
    text = unicodedata.normalize("NFKC", str(text)).lower()
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

    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

    if stem:
        stemmer = SnowballStemmer("english")
        tokens = [stemmer.stem(token) for token in tokens]

    return " ".join(tokens)


def add_text_features(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with reproducible text features."""
    validate_columns(df)
    out = df.copy()
    out["text"] = out["text"].fillna("").astype(str)
    out["char_count"] = out["text"].str.len()
    out["word_count"] = out["text"].str.findall(r"\b\w+\b").str.len()
    out["processed_text"] = out["text"].map(clean_text)
    return out
