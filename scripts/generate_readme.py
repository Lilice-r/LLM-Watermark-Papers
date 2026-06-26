from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader

from paperlib import (
    README_PATH,
    ROOT,
    TEMPLATES_DIR,
    TOPICS,
    TOPICS_DIR,
    group_by_timeline,
    load_papers,
    load_venues,
    paper_item_markdown,
    topic_link,
    venue_index,
)


def build_environment() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.globals["paper_item"] = paper_item_markdown
    env.globals["topic_link"] = topic_link
    return env


def render_all(papers: list[dict[str, Any]] | None = None) -> dict[Path, str]:
    papers = load_papers() if papers is None else papers
    venues = venue_index(load_venues())
    env = build_environment()

    output: dict[Path, str] = {}
    readme_template = env.get_template("README.md.j2")
    output[README_PATH] = readme_template.render(
        topics=TOPICS,
        timeline=group_by_timeline(papers, venues),
    )

    topic_template = env.get_template("topic.md.j2")
    for topic, label in TOPICS.items():
        topic_papers = [paper for paper in papers if topic in paper.get("topics", [])]
        output[TOPICS_DIR / f"{topic}.md"] = topic_template.render(
            topic=topic,
            label=label,
            timeline=group_by_timeline(topic_papers, venues),
        )

    return output


def write_all() -> None:
    for path, text in render_all().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README.md and topic pages from data/papers.yml.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero if generated files are out of date.")
    args = parser.parse_args()

    outputs = render_all()
    if args.check:
        changed = []
        for path, expected in outputs.items():
            actual = path.read_text(encoding="utf-8") if path.exists() else None
            if actual != expected:
                changed.append(path)
        if changed:
            for path in changed:
                print(f"out of date: {path.relative_to(ROOT)}")
            return 1
        print("generated files are up to date")
        return 0

    write_all()
    for path in outputs:
        print(f"generated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
