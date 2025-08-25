#!/usr/bin/env python3
"""
Script to generate a repository Table Of Contents (TOC).

This utility walks the project directory tree and writes a
``Table Of Contents.md`` file at the repository root.  The TOC uses a
bullet‑list style with relative links that are URL‑encoded, so the links
will work when viewed in GitHub.  You can configure which file
extensions are included, limit the depth of recursion, and supply
custom descriptions for particular entries.

To update the TOC manually run this script from any directory in the
repository:

    python Scripts/generate_repo_toc.py

The script always writes the TOC file.  It can be invoked via a CI
workflow to keep the TOC up‑to‑date automatically.
"""

from __future__ import annotations

import sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import quote

# Determine the repository root.  ``__file__`` refers to this script.
ROOT = Path(__file__).resolve().parents[1]

# Name of the markdown file to write relative to the root
TOC_FILE = ROOT / "Table Of Contents.md"

# ---------------- Configuration ----------------
# Names of directories to exclude from traversal
EXCLUDE_DIRS: set[str] = {
    ".git", "__pycache__", ".mypy_cache", ".pytest_cache",
    ".venv", "venv", "node_modules", "dist", "build", ".idea", ".vscode",
}

# Filenames to exclude
EXCLUDE_FILES: set[str] = {".DS_Store"}

# Allowed file extensions.  Set to ``None`` to include all files.
ALLOW_EXTS: set[str] | None = {
    ".md", ".py", ".ipynb", ".yml", ".yaml", ".toml",
}

# Maximum directory depth to traverse (0 = only top‑level).  Increase to
# include nested subdirectories.
MAX_DEPTH: int = 2

# Maximum number of items per directory.  Long lists are truncated.
MAX_ITEMS_PER_DIR: int = 100

# Whether to list folders before files in the TOC
FOLDERS_FIRST: bool = True

# Optional human‑readable descriptions to append after entries.  Keys
# should match relative paths or names.  Example:
# DESCRIPTIONS = {"docs": "Project documentation"}
DESCRIPTIONS: dict[str, str] = {}

def _urlencode_path(path: Path) -> str:
    """Return a URL‑encoded relative path for linking in markdown."""
    rel = path.relative_to(ROOT)
    # Use quote to percent‑encode special characters.  Do not encode path
    # separators (``/``) so that GitHub can interpret the path correctly.
    return quote(str(rel), safe="/")

def _write_entry(path: Path, depth: int, lines: list[str]) -> None:
    """Append a markdown list entry for ``path`` at the given depth."""
    indent = "  " * depth
    name = path.name
    link = _urlencode_path(path)
    entry = f"{indent}- [{name}]({link})"
    # Append description if provided
    desc_key = str(path.relative_to(ROOT))
    desc = DESCRIPTIONS.get(desc_key) or DESCRIPTIONS.get(name)
    if desc:
        entry += f" – {desc}"
    lines.append(entry)

def _traverse_dir(dir_path: Path, depth: int, lines: list[str]) -> None:
    """Recursively walk ``dir_path`` and collect TOC lines."""
    if depth > MAX_DEPTH:
        return
    try:
        children = [p for p in dir_path.iterdir() if p.name not in EXCLUDE_FILES]
    except PermissionError:
        # Skip directories we cannot access
        return
    entries: list[tuple[bool, Path]] = []
    for child in children:
        if child.is_dir():
            if child.name in EXCLUDE_DIRS:
                continue
            entries.append((True, child))
        else:
            if ALLOW_EXTS is not None and child.suffix not in ALLOW_EXTS:
                continue
            entries.append((False, child))
    # Optionally sort to put folders first, then sort alphabetically
    entries.sort(key=lambda item: (not FOLDERS_FIRST or not item[0], item[1].name.lower()))
    for is_dir, child in entries[:MAX_ITEMS_PER_DIR]:
        _write_entry(child, depth, lines)
        if is_dir:
            _traverse_dir(child, depth + 1, lines)

def generate_toc() -> list[str]:
    """Return a list of lines comprising the generated TOC."""
    lines: list[str] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    lines.append("# Table Of Contents")
    lines.append("")
    lines.append(f"_Generated on {timestamp}_")
    lines.append("")
    _traverse_dir(ROOT, 0, lines)
    return lines

def main() -> None:
    lines = generate_toc()
    TOC_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote table of contents to {TOC_FILE.relative_to(ROOT)} with {len(lines)} entries.")

if __name__ == "__main__":
    sys.exit(main())
