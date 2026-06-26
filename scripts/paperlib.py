from __future__ import annotations

import copy
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.yml"
README_PATH = ROOT / "README.md"
TOPICS_DIR = ROOT / "topics"
TEMPLATES_DIR = ROOT / "templates"

TOPICS: dict[str, str] = {
    "survey": "Survey",
    "zero-bit": "Zero-bit",
    "multi-bit": "Multi-bit",
    "attack": "Attack",
    "backdoor-watermark": "Backdoor Watermark",
}

# Colors for topic pages
"""
brightgreen
green
yellowgreen
yellow
orange
red
blue
lightgrey
grey
gray
blueviolet
success
important
critical
informational
inactive
"""
TOPIC_COLORS: dict[str, str] = {
    "survey": "brightgreen",
    "zero-bit": "yellowgreen",
    "multi-bit": "orange",
    "attack": "red",
    "backdoor-watermark": "blueviolet",
}

TRACKS = {"main", "findings", "journal", "workshop", "survey", "preprint"}

MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

VENUE_ORDER = {
    "NDSS": 10,
    "ICLR": 20,
    "NAACL": 30,
    "S&P": 40,
    "ACL": 50,
    "ICML": 60,
    "USENIX": 70,
    "CCS": 80,
    "EMNLP": 90,
    "NeurIPS": 100,
    "WIFS": 110,
    "AAAI": 120,
    "TMLR": 200,
    "TIFS": 210,
    "Nature": 220,
    "PMLR": 230,
    "ACM Computing Surveys": 240,
}

DEFAULT_MONTH_BY_VENUE = {
    "NDSS": 2,
    "ICLR": 4,
    "NAACL": 6,
    "S&P": 5,
    "ACL": 7,
    "ICML": 7,
    "USENIX": 8,
    "CCS": 10,
    "EMNLP": 11,
    "NeurIPS": 12,
    "WIFS": 12,
    "AAAI": 1,
}

MONTH_BY_VENUE_YEAR = {
    ("ACL", 2024): 8,
    ("ICLR", 2024): 5,
    ("NAACL", 2025): 4,
}


def load_papers(path: Path = DATA_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data is None:
        return []
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a list of paper records")
    return [normalize_paper(item) for item in data]


def save_papers(papers: list[dict[str, Any]], path: Path = DATA_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [normalize_paper(paper) for paper in papers]
    path.write_text(
        yaml.safe_dump(
            normalized,
            sort_keys=False,
            allow_unicode=True,
            width=4096,
        ),
        encoding="utf-8",
    )


def normalize_paper(paper: dict[str, Any]) -> dict[str, Any]:
    item = copy.deepcopy(paper)
    item["title"] = str(item.get("title", "")).strip()
    item["url"] = _clean_optional_string(item.get("url"))
    item["venue"] = str(item.get("venue", "")).strip()
    item["track"] = str(item.get("track") or "main").strip()
    item["topics"] = sorted({str(topic).strip() for topic in item.get("topics", []) if str(topic).strip()})

    if item.get("year") in ("", None):
        item["year"] = None
    else:
        item["year"] = int(item["year"])

    if item.get("month") in ("", None):
        item["month"] = None
    else:
        item["month"] = int(item["month"])

    item["award"] = _clean_optional_string(item.get("award"))
    item["badge"] = _clean_optional_string(item.get("badge"))
    item["notes"] = _clean_optional_string(item.get("notes"))
    return {key: value for key, value in item.items() if value not in (None, "", [])}


def _clean_optional_string(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def sort_key(paper: dict[str, Any]) -> tuple[Any, ...]:
    year = paper.get("year") or 9999
    month = paper.get("month") or default_month(paper.get("venue", ""), paper.get("year")) or 99
    venue = paper.get("venue", "")
    return (
        year,
        month,
        VENUE_ORDER.get(venue, 500),
        venue.lower(),
        paper.get("track") == "findings",
        paper.get("title", "").lower(),
    )


def sorted_papers(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(papers, key=sort_key)


def group_by_timeline(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_year: dict[Any, dict[tuple[Any, str], list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for paper in sorted_papers(papers):
        year = paper.get("year") or "Unknown Date"
        venue = paper.get("venue") or "Unknown Venue"
        month = paper.get("month") or default_month(venue, paper.get("year"))
        by_year[year][(month, venue)].append(paper)

    years = sorted(by_year, key=lambda value: value if isinstance(value, int) else 9999)
    result: list[dict[str, Any]] = []
    for year in years:
        venue_groups = []
        for (month, venue), group_papers in sorted(
            by_year[year].items(),
            key=lambda item: (
                item[0][0] or 99,
                VENUE_ORDER.get(item[0][1], 500),
                item[0][1].lower(),
            ),
        ):
            label = venue_group_label(venue, year, month)
            venue_groups.append({"label": label, "papers": group_papers})
        result.append({"year": year, "venues": venue_groups})
    return result


def default_month(venue: str, year: int | None = None) -> int | None:
    if year is not None and (venue, year) in MONTH_BY_VENUE_YEAR:
        return MONTH_BY_VENUE_YEAR[(venue, year)]
    return DEFAULT_MONTH_BY_VENUE.get(venue)


def venue_group_label(venue: str, year: Any, month: int | None = None) -> str:
    if year == "Unknown Date":
        return venue
    month_text = f" ({MONTH_NAMES[month]})" if month else ""
    return f"{venue} {year}{month_text}"


def badge_text(paper: dict[str, Any]) -> str:
    if paper.get("badge"):
        return str(paper["badge"])
    venue = paper.get("venue", "")
    year = paper.get("year")
    text = f"{venue} {year}".strip() if year else venue
    if paper.get("track") == "findings":
        text = f"{text} Findings"
    if paper.get("award"):
        text = f"{text}-{paper['award']}"
    return text


def badge_markdown(paper: dict[str, Any]) -> str:
    text = badge_text(paper)
    return f"![](https://img.shields.io/badge/{quote(text, safe='')}-orange)"


def shields_text(text: str) -> str:
    return quote(text.replace("-", "--"), safe="")


def venue_label(paper: dict[str, Any]) -> str:
    venue = paper.get("venue", "")
    year = paper.get("year")
    text = f"{venue} {year}".strip() if year else venue
    if paper.get("track") == "findings":
        text = f"{text} Findings"
    if paper.get("award"):
        award = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", str(paper["award"]))
        text = f"{text} ({award})"
    return text


def topic_link(topic: str, prefix: str = "topics/") -> str:
    label = TOPICS.get(topic, topic)
    color = TOPIC_COLORS.get(topic, "57606a")
    badge = f"![{label}](https://img.shields.io/badge/{shields_text(label)}-{color})"
    return f"[{badge}]({prefix}{topic}.md)"


def paper_item_markdown(
    paper: dict[str, Any],
    *,
    include_topics: bool = False,
    topic_prefix: str = "topics/",
) -> str:
    url = paper.get("url") or ""
    details = [f"[paper]({url})" if url else "paper: TBD", venue_label(paper)]
    if include_topics:
        details.extend(topic_link(topic, prefix=topic_prefix) for topic in paper.get("topics", []))
    return f"- **{paper['title']}**  \n  {' | '.join(details)}"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "paper"


def check_papers(papers: list[dict[str, Any]]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    title_to_papers: dict[str, list[dict[str, Any]]] = defaultdict(list)
    url_to_papers: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for index, paper in enumerate(papers, start=1):
        where = f"record {index}"
        title = paper.get("title", "")
        if not title:
            errors.append(f"{where}: missing title")
        else:
            title_to_papers[title.casefold()].append(paper)

        if not paper.get("url"):
            warnings.append(f"{where}: missing paper URL for '{title}'")
        else:
            url_to_papers[str(paper["url"]).strip()].append(paper)

        if not paper.get("venue"):
            errors.append(f"{where}: missing venue for '{title}'")
        if not paper.get("year"):
            warnings.append(f"{where}: missing year for '{title}'")
        if paper.get("month") and not 1 <= int(paper["month"]) <= 12:
            errors.append(f"{where}: month must be between 1 and 12 for '{title}'")
        if paper.get("track") not in TRACKS:
            errors.append(f"{where}: unknown track '{paper.get('track')}' for '{title}'")

        for topic in paper.get("topics", []):
            if topic not in TOPICS:
                errors.append(f"{where}: unknown topic '{topic}' for '{title}'")

        if re.search(r"鈥|檛|�", title):
            warnings.append(f"{where}: title may contain mojibake: '{title}'")

        url = paper.get("url") or ""
        track = paper.get("track")
        if "findings-acl" in url and track != "findings":
            errors.append(f"{where}: ACL Findings URL but track is '{track}' for '{title}'")
        if "acl-long" in url and track == "findings":
            errors.append(f"{where}: ACL long URL but track is Findings for '{title}'")
        if "findings-naacl" in url and track != "findings":
            errors.append(f"{where}: NAACL Findings URL but track is '{track}' for '{title}'")
        if "naacl-long" in url and track == "findings":
            errors.append(f"{where}: NAACL long URL but track is Findings for '{title}'")
        if "findings-emnlp" in url and track != "findings":
            errors.append(f"{where}: EMNLP Findings URL but track is '{track}' for '{title}'")
        if "emnlp-main" in url and track == "findings":
            errors.append(f"{where}: EMNLP main URL but track is Findings for '{title}'")

    for title, matches in title_to_papers.items():
        if len(matches) > 1:
            errors.append(f"duplicate title: '{matches[0].get('title')}' appears {len(matches)} times")

    for url, matches in url_to_papers.items():
        distinct_titles = sorted({paper.get("title", "") for paper in matches})
        if len(distinct_titles) > 1:
            errors.append(f"duplicate URL used by multiple titles: {url} -> {', '.join(distinct_titles)}")

    return errors, warnings
