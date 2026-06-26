from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run_step(label: str, command: list[str], *, required: bool = True) -> bool:
    print(f"\n== {label} ==", flush=True)
    completed = subprocess.run(command, cwd=ROOT)
    if completed.returncode == 0:
        return True

    if required:
        print(f"\nPipeline stopped at: {label}", flush=True)
        return False

    print(f"\nNon-blocking step failed: {label}", flush=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the post-edit paper-list pipeline after manually editing data/papers.yml."
    )
    parser.add_argument("--skip-git", action="store_true", help="Skip git status and diff summary.")
    args = parser.parse_args()

    python = sys.executable
    steps = [
        (
            "Validate data/papers.yml",
            [python, str(SCRIPTS / "check_format.py"), "--skip-generated"],
            True,
        ),
        (
            "Generate README.md and topic pages",
            [python, str(SCRIPTS / "generate_readme.py")],
            True,
        ),
        (
            "Validate generated markdown",
            [python, str(SCRIPTS / "check_format.py")],
            True,
        ),
        (
            "Confirm generated files are up to date",
            [python, str(SCRIPTS / "generate_readme.py"), "--check"],
            True,
        ),
    ]

    if not args.skip_git:
        steps.extend(
            [
                ("Show git status", ["git", "status", "--short"], False),
                ("Show diff summary", ["git", "diff", "--stat"], False),
            ]
        )

    for label, command, required in steps:
        if not run_step(label, command, required=required):
            return 1

    print("\nPipeline completed.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
