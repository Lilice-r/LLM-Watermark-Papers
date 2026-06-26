from __future__ import annotations

import argparse
import re

from generate_readme import render_all
from paperlib import DATA_PATH, ROOT, check_papers, load_papers


EMPTY_PAPER_LINK = re.compile(r"\[\[paper\]\]\(\)")
MALFORMED_PAPER_LINK = re.compile(r"\[\[paper\]\([^)]*\)\]")


def check_generated_files() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for path, expected in render_all().items():
        if not path.exists():
            errors.append(f"missing generated file: {path.relative_to(ROOT)}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected:
            errors.append(f"generated file is out of date: {path.relative_to(ROOT)}")
        if MALFORMED_PAPER_LINK.search(actual):
            errors.append(f"malformed paper link in {path.relative_to(ROOT)}")
        if EMPTY_PAPER_LINK.search(actual):
            warnings.append(f"empty paper link in {path.relative_to(ROOT)}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check paper data and generated markdown files.")
    parser.add_argument(
        "--skip-generated",
        action="store_true",
        help="Only validate data/papers.yml, without checking generated markdown files.",
    )
    args = parser.parse_args()

    if not DATA_PATH.exists():
        print(f"error: missing {DATA_PATH.relative_to(ROOT)}")
        return 1

    errors, warnings = check_papers(load_papers())
    if not args.skip_generated:
        generated_errors, generated_warnings = check_generated_files()
        errors.extend(generated_errors)
        warnings.extend(generated_warnings)

    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")

    if errors:
        print(f"check failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"check passed: {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
