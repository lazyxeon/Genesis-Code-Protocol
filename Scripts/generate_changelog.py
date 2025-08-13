#!/usr/bin/env python3
"""
Generate/refresh CHANGELOG.md from git history (Conventional Commit-ish).
- Groups commits since last tag into categories (feat, fix, docs, refactor, chore, perf, test, build, ci).
- If no tags exist, uses the first commit as the start.
- Writes/updates a top "## [Unreleased]" section (no tagging).
- Links commits and PRs for GitHub view.
Run in GitHub Actions or locally.
"""

from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Tuple, Dict

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
REPO = os.getenv("GITHUB_REPOSITORY", "")  # e.g. "lazyxeon/Genesis-Code-Protocol"
GH_BASE = os.getenv("GITHUB_SERVER_URL", "https://github.com").rstrip("/")

CC_ORDER = ["feat", "fix", "perf", "refactor", "docs", "test", "build", "ci", "chore", "other"]
HEAD_RE = re.compile(r"^(?P<type>[a-z]+)(\((?P<scope>[^)]+)\))?[: ]\s*(?P<msg>.+)$", re.IGNORECASE)
PR_RE = re.compile(r"\(#(?P<num>\d+)\)")  # matches "(#123)"

def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "replace").strip()

def last_tag() -> str | None:
    try:
        return run("git", "describe", "--tags", "--abbrev=0")
    except subprocess.CalledProcessError:
        return None

def commits_since(tag: str | None) -> List[Tuple[str, str]]:
    rng = f"{tag}..HEAD" if tag else "--reverse --max-parents=1 HEAD"
    fmt = "%H%x09%s"
    if tag:
        log = run("git", "log", rng, f"--pretty=format:{fmt}")
    else:
        # from the first commit to HEAD
        first = run("git", "rev-list", "--max-parents=0", "HEAD").splitlines()[0]
        log = run("git", "log", f"{first}..HEAD", f"--pretty=format:{fmt}")
    lines = [l for l in log.splitlines() if l and not l.lower().startswith("merge pull request")]
    pairs = []
    for l in lines:
        try:
            h, s = l.split("\t", 1)
        except ValueError:
            parts = l.split(" ", 1)
            h, s = parts[0], (parts[1] if len(parts) > 1 else "")
        pairs.append((h, s))
    return pairs

def classify(subject: str) -> Tuple[str, str, str | None]:
    m = HEAD_RE.match(subject)
    if not m:
        return "other", subject.strip(), None
    typ = m.group("type").lower()
    scope = m.group("scope")
    msg = m.group("msg").strip()
    if typ not in CC_ORDER:
        typ = "other"
    return typ, msg, scope

def commit_link(hash_: str) -> str:
    short = hash_[:7]
    if REPO:
        return f"[{short}]({GH_BASE}/{REPO}/commit/{hash_})"
    return short

def pr_link(subject: str) -> str | None:
    m = PR_RE.search(subject)
    if not m or not REPO:
        return None
    n = m.group("num")
    return f"[#{n}]({GH_BASE}/{REPO}/pull/{n})"

def build_section(commits: List[Tuple[str, str]]) -> str:
    cats: Dict[str, List[str]] = {k: [] for k in CC_ORDER}
    for h, s in commits:
        typ, msg, scope = classify(s)
        pr = pr_link(s)
        scope_txt = f"**{scope}**: " if scope else ""
        tail = f" {pr}" if pr else ""
        cats[typ].append(f"- {scope_txt}{msg} ({commit_link(h)}){tail}")

    lines = []
    for cat in CC_ORDER:
        items = [i for i in cats[cat] if i]
        if not items:
            continue
        title = {
            "feat": "Features",
            "fix": "Fixes",
            "perf": "Performance",
            "refactor": "Refactors",
            "docs": "Documentation",
            "test": "Tests",
            "build": "Build",
            "ci": "CI",
            "chore": "Chores",
            "other": "Other",
        }[cat]
        lines.append(f"### {title}")
        lines.extend(items)
        lines.append("")  # blank line
    return "\n".join(lines).rstrip() + ("\n" if lines else "")

def render(commits: List[Tuple[str, str]]) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    header = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
    unreleased = f"## [Unreleased] — {today}\n\n"
    body = build_section(commits) or "_No changes since last tag._\n"
    return header + unreleased + body

def update_file(text: str) -> None:
    if CHANGELOG.exists():
        old = CHANGELOG.read_text(encoding="utf-8")
        # Replace existing [Unreleased] section; if not present, prepend.
        pattern = re.compile(r"^## \[Unreleased\].*?(?=^## |\Z)", flags=re.DOTALL | re.MULTILINE)
        if pattern.search(old):
            new = pattern.sub(text.split("## [Unreleased]")[1].join(["## [Unreleased]", ""]), old, count=1)
        else:
            new = text + "\n" + old
        CHANGELOG.write_text(new, encoding="utf-8", newline="\n")
    else:
        CHANGELOG.write_text(text, encoding="utf-8", newline="\n")

def main() -> int:
    tag = last_tag()
    commits = commits_since(tag)
    out = render(commits)
    update_file(out)
    print(f"CHANGELOG updated. Last tag: {tag or 'None'}; commits counted: {len(commits)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
