import pandas as pd
import pytest

from src.comparative_analysis import cross_region_similarity_summary, fit_kmeans_tfidf, top_terms_per_cluster
from src.network_analysis import build_country_mention_network, centrality_table
from src.preprocessing import add_coursework_continent, filter_africa, filter_africa_europe, validate_columns


def toy_frame():
    return pd.DataFrame(
        {
            "country": ["NGA", "KEN", "FRA", "ITA", "USA"],
            "session": [50, 50, 50, 50, 50],
            "year": [1995] * 5,
            "text": [
                "Nigeria supports peace and Kenya.",
                "Kenya discusses development and Nigeria.",
                "France supports European cooperation.",
                "Italy discusses European cooperation.",
                "United States statement.",
            ],
        }
    )


def test_continent_mapping_and_filters():
    df = add_coursework_continent(toy_frame())
    assert df.loc[df.country.eq("NGA"), "Continent"].iat[0] == "Africa"
    assert df.loc[df.country.eq("FRA"), "Continent"].iat[0] == "Europe"
    assert pd.isna(df.loc[df.country.eq("USA"), "Continent"].iat[0])
    assert set(filter_africa(df).country) == {"NGA", "KEN"}
    assert set(filter_africa_europe(df).country) == {"NGA", "KEN", "FRA", "ITA"}


def test_validate_columns():
    with pytest.raises(ValueError):
        validate_columns(pd.DataFrame({"text": ["x"]}))


def test_similarity_estimands_are_well_defined():
    docs = ["peace development", "peace security", "europe trade", "europe market"]
    groups = ["Africa", "Africa", "Europe", "Europe"]
    result = cross_region_similarity_summary(docs, groups, pair_sample_size=2, random_state=1)
    for value in (result.coursework_first_pair, result.centroid_cosine, result.sampled_pairwise_mean):
        assert 0.0 <= value <= 1.0
    assert result.pair_sample_size == 2


def test_kmeans_outputs_terms():
    docs = [
        "peace security development africa",
        "peace security africa",
        "trade market economy europe",
        "trade economy europe",
    ]
    result = fit_kmeans_tfidf(docs, n_clusters=2, random_state=42)
    assert len(result.labels) == 4
    terms = top_terms_per_cluster(result, top_n=3)
    assert list(terms.columns) == ["cluster", "top_terms"]
    assert len(terms) == 2


def test_network_mentions_names_and_aliases():
    df = pd.DataFrame(
        {
            "country": ["NGA", "KEN", "COD"],
            "text": [
                "Nigeria welcomes cooperation with Kenya and South Africa.",
                "Kenya mentions Nigeria and Zaire.",
                "The Democratic Republic of the Congo thanks Kenya.",
            ],
        }
    )
    graph = build_country_mention_network(df)
    assert graph.has_edge("NGA", "KEN")
    assert graph.has_edge("NGA", "ZAF")
    assert graph.has_edge("KEN", "NGA")
    assert graph.has_edge("KEN", "COD")
    table = centrality_table(graph)
    assert {"country", "in_strength", "out_strength"}.issubset(table.columns)
