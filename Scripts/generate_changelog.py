#!/usr/bin/env python3
"""
Generate/refresh CHANGELOG.md from git history (Conventional-Commit-ish).

- Groups commits since last tag into categories (feat, fix, perf, refactor, docs, test, build, ci, chore, other).
- If no tags exist, uses first commit → HEAD.
- Updates or creates a top "## [Unreleased] — YYYY-MM-DD" section.
- Preserves the rest of the file (older releases).
- Adds commit and PR links when running in GitHub Actions.
"""

from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Tuple, Dict

ROOT = Path(__file__).resolve().parents[1]
CHANGELOG = ROOT / "CHANGELOG.md"
REPO = os.getenv("GITHUB_REPOSITORY", "")          # e.g. "lazyxeon/Genesis-Code-Protocol"
GH_BASE = os.getenv("GITHUB_SERVER_URL", "https://github.com").rstrip("/")

CC_ORDER = ["feat", "fix", "perf", "refactor", "docs", "test", "build", "ci", "chore", "other"]
HEAD_RE = re.compile(r"^(?P<type>[a-z]+)(\((?P<scope>[^)]+)\))?[: ]\s*(?P<msg>.+)$", re.IGNORECASE)
PR_RE = re.compile(r"\(#(?P<num>\d+)\)")

def sh(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT).decode("utf-8", "replace").strip()

def last_tag() -> str | None:
    try:
        return sh("git", "describe", "--tags", "--abbrev=0")
    except subprocess.CalledProcessError:
        return None

def commits_since(tag: str | None) -> List[Tuple[str, str]]:
    fmt = "%H%x09%s"
    if tag:
        log = sh("git", "log", f"{tag}..HEAD", f"--pretty=format:{fmt}")
    else:
        first = sh("git", "rev-list", "--max-parents=0", "HEAD").splitlines()[0]
        log = sh("git", "log", f"{first}..HEAD", f"--pretty=format:{fmt}")
    pairs: List[Tuple[str, str]] = []
    for line in log.splitlines():
        if not line:
            continue
        # ignore merge noise
        subj = line.split("\t", 1)[1] if "\t" in line else line
        if subj.lower().startswith("merge"):
            continue
        commit, subject = line.split("\t", 1) if "\t" in line else (line[:40], subj)
        pairs.append((commit, subject))
    return pairs

def classify(subject: str) -> Tuple[str, str, str | None]:
    m = HEAD_RE.match(subject)
    if not m:
        return "other", subject.strip(), None
    typ = m.group("type").lower()
    if typ not in CC_ORDER:
        typ = "other"
    return typ, m.group("msg").strip(), m.group("scope")

def link_commit(h: str) -> str:
    shash = h[:7]
    return f"[{shash}]({GH_BASE}/{REPO}/commit/{h})" if REPO else shash

def link_pr(subject: str) -> str | None:
    m = PR_RE.search(subject)
    if not (m and REPO):
        return None
    n = m.group("num")
    return f"[#{n}]({GH_BASE}/{REPO}/pull/{n})"

def build_section(commits: List[Tuple[str,str]]) -> str:
    buckets: Dict[str, List[str]] = {k: [] for k in CC_ORDER}
    for h, s in commits:
        typ, msg, scope = classify(s)
        pr = link_pr(s)
        scope_txt = f"**{scope}**: " if scope else ""
        pr_txt = f" {pr}" if pr else ""
        buckets[typ].append(f"- {scope_txt}{msg} ({link_commit(h)}){pr_txt}")
    lines: List[str] = []
    titles = {
        "feat": "Features", "fix": "Fixes", "perf": "Performance",
        "refactor": "Refactors", "docs": "Documentation", "test": "Tests",
        "build": "Build", "ci": "CI", "chore": "Chores", "other": "Other",
    }
    for cat in CC_ORDER:
        items = buckets[cat]
        if not items:
            continue
        lines.append(f"### {titles[cat]}")
        lines.extend(items)
        lines.append("")
    return "\n".join(lines).rstrip() + ("\n" if lines else "")

def render_unreleased(commits: List[Tuple[str,str]]) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    body = build_section(commits) or "_No changes since last tag._\n"
    return f"## [Unreleased] — {today}\n\n{body}"

def update_changelog(unreleased: str) -> str:
    header = "# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n"
    if CHANGELOG.exists():
        old = CHANGELOG.read_text(encoding="utf-8")
        # Ensure single header at top
        if old.startswith("# Changelog"):
            base = old
        else:
            base = header + old
        # Replace or insert Unreleased section
        pat = re.compile(r"^## \[Unreleased\].*?(?=^## |\Z)", re.DOTALL | re.MULTILINE)
        if pat.search(base):
            new = pat.sub(unreleased + "\n", base, count=1)
        else:
            # insert after header
            if base.startswith(header):
                new = header + unreleased + "\n" + base[len(header):]
            else:
                new = unreleased + "\n" + base
        return new
    else:
        return header + unreleased + "\n"

def main() -> int:
    try:
        tag = last_tag()
        commits = commits_since(tag)
        print(f"Last_tag={tag or 'None'}; commit_count={len(commits)}")
        unreleased = render_unreleased(commits)
        new_text = update_changelog(unreleased)
        CHANGELOG.write_text(new_text, encoding="utf-8", newline="\n")
        print("CHANGELOG.md written/updated.")
        return 0
    except Exception as e:
        print(f"::error::Changelog generation failed: {e}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
