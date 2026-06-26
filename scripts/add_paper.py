from __future__ import annotations

import argparse
from typing import Any

from generate_readme import write_all
from paperlib import (
    TOPICS,
    TRACKS,
    check_papers,
    check_venues,
    load_papers,
    load_venues,
    normalize_paper,
    normalize_venue,
    save_papers,
    save_venues,
    venue_key,
)


def prompt_if_missing(value: Any, label: str, *, required: bool = True) -> Any:
    if value not in (None, "", []):
        return value
    suffix = "" if required else " (optional)"
    while True:
        entered = input(f"{label}{suffix}: ").strip()
        if entered or not required:
            return entered or None


def parse_topics(values: list[str] | None) -> list[str]:
    if not values:
        return []
    topics: list[str] = []
    for value in values:
        topics.extend(part.strip() for part in value.split(",") if part.strip())
    return topics


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add one paper, create a venue-year mapping when needed, and regenerate markdown pages."
    )
    parser.add_argument("--title")
    parser.add_argument("--url")
    parser.add_argument("--venue")
    parser.add_argument("--year", type=int)
    parser.add_argument("--venue-month", type=int, help="Month for a new venue/year mapping.")
    parser.add_argument("--venue-order", type=int, help="Sort order for a new venue/year mapping.")
    parser.add_argument("--track", default="main", choices=sorted(TRACKS))
    parser.add_argument("--topics", nargs="*", help=f"Space- or comma-separated topics: {', '.join(TOPICS)}")
    parser.add_argument("--award")
    parser.add_argument("--notes")
    parser.add_argument("--allow-duplicate", action="store_true")
    parser.add_argument("--no-generate", action="store_true", help="Only update data/papers.yml.")
    args = parser.parse_args()

    title = prompt_if_missing(args.title, "Title")
    venue = prompt_if_missing(args.venue, "Venue")
    year = args.year or int(prompt_if_missing(None, "Year"))
    venues = load_venues()
    venue_lookup = {venue_key(item["venue"], item["year"]): item for item in venues}
    candidate_venues = list(venues)
    if venue_key(venue, year) not in venue_lookup:
        month = args.venue_month
        if month is None:
            month = int(prompt_if_missing(None, f"Month number for {venue} {year}"))
        order = args.venue_order
        if order is None:
            previous_orders = [item["order"] for item in venues if item.get("venue") == venue and "order" in item]
            order = previous_orders[0] if previous_orders else 500
        candidate_venues.append(normalize_venue({"venue": venue, "year": year, "month": month, "order": order}))

    topics = parse_topics(args.topics)
    if not topics:
        topics_text = prompt_if_missing(
            None,
            f"Topics ({', '.join(TOPICS)})",
        )
        topics = parse_topics([topics_text])

    unknown_topics = [topic for topic in topics if topic not in TOPICS]
    if unknown_topics:
        print(f"error: unknown topic(s): {', '.join(unknown_topics)}")
        return 1

    paper = normalize_paper(
        {
            "title": title,
            "url": prompt_if_missing(args.url, "Paper URL", required=False),
            "venue": venue,
            "year": year,
            "track": args.track,
            "topics": topics,
            "award": args.award,
            "notes": args.notes,
        }
    )

    papers = load_papers()
    if not args.allow_duplicate:
        title_key = paper["title"].casefold()
        url = paper.get("url")
        for existing in papers:
            if existing.get("title", "").casefold() == title_key:
                print(f"error: duplicate title already exists: {existing['title']}")
                return 1
            if url and existing.get("url") == url:
                print(f"error: duplicate URL already exists for: {existing['title']}")
                return 1

    candidate = papers + [paper]
    venue_errors, venue_warnings = check_venues(candidate_venues)
    paper_errors, paper_warnings = check_papers(candidate, candidate_venues)
    errors = venue_errors + paper_errors
    warnings = venue_warnings + paper_warnings
    for warning in warnings:
        print(f"warning: {warning}")
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    save_venues(candidate_venues)
    save_papers(candidate)
    if not args.no_generate:
        write_all()
    print(f"added: {paper['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
