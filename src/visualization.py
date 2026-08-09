"""Publication-style plotting helpers for the UNGD analysis."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


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


def plot_word_count_distribution(df: pd.DataFrame):
    """Plot raw speech word counts and return (fig, ax)."""
    if "word_count" not in df.columns:
        raise ValueError("Run add_text_features before plotting word counts.")

    median = float(df["word_count"].median())
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.hist(df["word_count"], bins=30, alpha=0.9)
    ax.axvline(median, linestyle="--", linewidth=1.8, label=f"Median: {median:,.0f} words")
    ax.set_title("Speech length distribution", loc="left")
    ax.set_xlabel("Words per speech")
    ax.set_ylabel("Number of speeches")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.20)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    return fig, ax
