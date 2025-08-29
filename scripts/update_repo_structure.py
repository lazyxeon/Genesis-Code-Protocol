#!/usr/bin/env python3
"""Update the repository README with a file tree section."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

# Tweak as needed
EXCLUDE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
}
EXCLUDE_FILES = {".DS_Store"}

MAX_DEPTH = 2  # increase to 3+ if you want deeper trees
MAX_ENTRIES = 500  # safety cap per directory

BEGIN = "<!-- BEGIN:REPO_STRUCTURE -->"
END = "<!-- END:REPO_STRUCTURE -->"


def build_tree(root: Path, prefix: str = "", depth: int = 0) -> str:
    """Return a markdown-friendly tree listing of files and directories."""
    if depth > MAX_DEPTH:
        return ""

    try:
        names = sorted(os.listdir(root))
    except OSError:
        return ""

    # Filter excluded entries and enforce MAX_ENTRIES limit
    entries: list[tuple[str, Path]] = []
    for name in names:
        if name in EXCLUDE_FILES:
            continue
        path = root / name
        if path.is_dir() and name in EXCLUDE_DIRS:
            continue
        entries.append((name, path))
        if len(entries) >= MAX_ENTRIES:
            break

    lines = []
    for idx, (name, path) in enumerate(entries):
        connector = "└── " if idx == len(entries) - 1 else "├── "
        if path.is_dir():
            lines.append(f"{prefix}{connector}{name}/")
            extension = "    " if idx == len(entries) - 1 else "│   "
            subtree = build_tree(path, prefix + extension, depth + 1)
            if subtree:
                lines.append(subtree)
        else:
            lines.append(f"{prefix}{connector}{name}")

    return "\n".join(lines)


def replace_between(text: str, start: str, end: str, new_block: str) -> str:
    """Insert ``new_block`` between ``start`` and ``end`` markers in ``text``."""
    pat = re.compile(rf"({re.escape(start)})(.*?){re.escape(end)}", re.DOTALL)
    repl = f"{start}\n```\n{new_block}\n```\n{end}"
    if pat.search(text):
        return pat.sub(repl, text, count=1)

    # Fallback: insert after the heading if markers are missing
    heading = re.search(r"^## Repository Structure\s*$", text, flags=re.MULTILINE)
    if heading:
        insert_pos = heading.end()
        return text[:insert_pos] + "\n\n" + repl + "\n" + text[insert_pos:]

    # If heading also missing, append a new section at the end
    extra = f"\n\n## Repository Structure\n\n{repl}\n"
    return text + extra


def main() -> None:
    """Regenerate the repository tree section in README.md."""
    if not README.exists():
        print("README.md not found at repo root.", file=sys.stderr)
        sys.exit(1)

    content = README.read_text(encoding="utf-8")
    tree = build_tree(ROOT) or "(empty)"
    updated = replace_between(content, BEGIN, END, tree)

    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated with repository tree.")
    else:
        print("No changes needed (tree unchanged or markers absent).")


if __name__ == "__main__":
    main()
