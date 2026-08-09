"""Publication-style plotting helpers for the combined UNGD analysis."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def plot_speeches_over_time(df: pd.DataFrame):
    """Plot the number of speeches by year and return (fig, ax)."""
    counts = df.groupby("year").size().sort_index()
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(counts.index, counts.values, linewidth=2.2)
    ax.set_title("African UN General Debate speeches in the analysis sample", loc="left")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of speeches")
    ax.grid(axis="y", alpha=0.25)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig, ax


def plot_word_count_distribution(df: pd.DataFrame, *, title: str = "Speech length distribution"):
    """Plot raw speech word counts and return (fig, ax)."""
    if "word_count" not in df.columns:
        raise ValueError("Run add_text_features before plotting word counts.")

    median = float(df["word_count"].median())
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.hist(df["word_count"], bins=30, alpha=0.9)
    ax.axvline(median, linestyle="--", linewidth=1.8, label=f"Median: {median:,.0f} words")
    ax.set_title(title, loc="left")
    ax.set_xlabel("Words per speech")
    ax.set_ylabel("Number of speeches")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.20)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig, ax


def make_wordcloud(
    documents: pd.Series | list[str],
    *,
    title: str,
    max_words: int = 250,
    width: int = 1200,
    height: int = 650,
):
    """Create a word cloud from a sequence of already-cleaned documents."""
    text = " ".join(str(doc) for doc in documents if str(doc).strip())
    cloud = WordCloud(
        width=width,
        height=height,
        max_words=max_words,
        background_color="white",
        collocations=False,
    ).generate(text)
    fig, ax = plt.subplots(figsize=(12, 6.5))
    ax.imshow(cloud, interpolation="bilinear")
    ax.axis("off")
    ax.set_title(title, loc="left")
    fig.tight_layout()
    return fig, ax


def plot_sentiment_over_time(
    df: pd.DataFrame,
    *,
    score_column: str = "sentiment_compound",
    group_column: str | None = None,
    title: str = "VADER sentiment over time",
):
    """Plot annual mean speech-level sentiment, optionally by region."""
    required = {"year", score_column}
    if group_column:
        required.add(group_column)
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    fig, ax = plt.subplots(figsize=(10, 5))
    if group_column:
        annual = (
            df.groupby(["year", group_column], as_index=False)[score_column]
            .mean()
            .sort_values("year")
        )
        for label, part in annual.groupby(group_column):
            ax.plot(part["year"], part[score_column], linewidth=2, label=str(label))
        ax.legend(frameon=False)
    else:
        annual = df.groupby("year")[score_column].mean().sort_index()
        ax.plot(annual.index, annual.values, linewidth=2)

    ax.axhline(0, linewidth=1, alpha=0.4)
    ax.set_title(title, loc="left")
    ax.set_xlabel("Year")
    ax.set_ylabel("Mean VADER compound score")
    ax.grid(axis="y", alpha=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig, ax


def plot_cluster_distribution(labels, *, title: str = "K-means cluster distribution"):
    """Plot document counts by K-means cluster."""
    counts = pd.Series(labels).value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title(title, loc="left")
    ax.set_xlabel("Cluster")
    ax.set_ylabel("Documents")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig, ax
