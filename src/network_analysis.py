"""Country-mention network utilities for the Africa-focused SMWA extension.

The submitted coursework constructed a directed weighted graph linking an
African speaker country to other African countries mentioned in its statement.
This professional implementation matches country *names* (and optionally ISO3
codes) in the original speech text, making the measurement rule explicit.
"""

from __future__ import annotations

import re
from collections import Counter

import networkx as nx
import pandas as pd


AFRICAN_COUNTRIES = {
    "DZA": "Algeria", "AGO": "Angola", "BEN": "Benin", "BWA": "Botswana",
    "BFA": "Burkina Faso", "BDI": "Burundi", "CPV": "Cabo Verde",
    "CMR": "Cameroon", "CAF": "Central African Republic", "TCD": "Chad",
    "COM": "Comoros", "COD": "Democratic Republic of the Congo",
    "COG": "Republic of the Congo", "DJI": "Djibouti", "EGY": "Egypt",
    "GNQ": "Equatorial Guinea", "ERI": "Eritrea", "SWZ": "Eswatini",
    "ETH": "Ethiopia", "GAB": "Gabon", "GMB": "Gambia", "GHA": "Ghana",
    "GIN": "Guinea", "GNB": "Guinea-Bissau", "CIV": "Cote d'Ivoire",
    "KEN": "Kenya", "LSO": "Lesotho", "LBR": "Liberia", "LBY": "Libya",
    "MDG": "Madagascar", "MWI": "Malawi", "MLI": "Mali",
    "MRT": "Mauritania", "MUS": "Mauritius", "MAR": "Morocco",
    "MOZ": "Mozambique", "NAM": "Namibia", "NER": "Niger", "NGA": "Nigeria",
    "RWA": "Rwanda", "STP": "Sao Tome and Principe", "SEN": "Senegal",
    "SYC": "Seychelles", "SLE": "Sierra Leone", "SOM": "Somalia",
    "ZAF": "South Africa", "SSD": "South Sudan", "SDN": "Sudan",
    "TZA": "Tanzania", "TGO": "Togo", "TUN": "Tunisia", "UGA": "Uganda",
    "ZMB": "Zambia", "ZWE": "Zimbabwe",
}

# Common historical/orthographic variants useful for the 1970-2015 corpus.
ALIASES = {
    "COD": ["Democratic Republic of the Congo", "DR Congo", "Zaire"],
    "COG": ["Republic of the Congo", "Congo-Brazzaville"],
    "CIV": ["Cote d'Ivoire", "Côte d’Ivoire", "Ivory Coast"],
    "CPV": ["Cabo Verde", "Cape Verde"],
    "SWZ": ["Eswatini", "Swaziland"],
    "TZA": ["Tanzania", "United Republic of Tanzania"],
}


def _patterns(include_iso_codes: bool = False) -> dict[str, re.Pattern[str]]:
    patterns: dict[str, re.Pattern[str]] = {}
    for code, name in AFRICAN_COUNTRIES.items():
        terms = list(ALIASES.get(code, [name]))
        if name not in terms:
            terms.append(name)
        if include_iso_codes:
            terms.append(code)
        escaped = sorted((re.escape(term) for term in terms), key=len, reverse=True)
        patterns[code] = re.compile(r"(?<!\w)(?:" + "|".join(escaped) + r")(?!\w)", re.I)
    return patterns


def build_country_mention_network(
    speeches: pd.DataFrame,
    *,
    country_column: str = "country",
    text_column: str = "text",
    include_iso_codes: bool = False,
) -> nx.DiGraph:
    """Build a directed weighted network of African country mentions.

    A directed edge A -> B receives one count for every speech by country A
    that contains a textual mention of country B. Multiple mentions within the
    same speech count once; this avoids mechanically overweighting repetition.
    """
    missing = {country_column, text_column}.difference(speeches.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    patterns = _patterns(include_iso_codes=include_iso_codes)
    counts: Counter[tuple[str, str]] = Counter()

    africa = speeches.loc[speeches[country_column].isin(AFRICAN_COUNTRIES)].copy()
    for _, row in africa.iterrows():
        speaker = str(row[country_column])
        text = str(row[text_column])
        for mentioned, pattern in patterns.items():
            if mentioned != speaker and pattern.search(text):
                counts[(speaker, mentioned)] += 1

    graph = nx.DiGraph()
    for code, name in AFRICAN_COUNTRIES.items():
        graph.add_node(code, name=name)
    for (source, target), weight in counts.items():
        graph.add_edge(source, target, weight=int(weight))
    return graph


def centrality_table(graph: nx.DiGraph) -> pd.DataFrame:
    """Return descriptive degree/strength measures for the mention network."""
    rows = []
    for node in graph.nodes:
        rows.append(
            {
                "country": node,
                "country_name": graph.nodes[node].get("name", node),
                "in_degree": graph.in_degree(node),
                "out_degree": graph.out_degree(node),
                "in_strength": graph.in_degree(node, weight="weight"),
                "out_strength": graph.out_degree(node, weight="weight"),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["in_strength", "in_degree"], ascending=False, ignore_index=True
    )
