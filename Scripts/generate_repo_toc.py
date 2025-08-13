#!/usr/bin/env python3
"""
Generate a repository Table of Contents in 'Table Of Contents.md' (root).
- Works with GitHub rendering: relative links, URL-encoded paths.
- Bullet-list style, folders first, depth-bounded.
- Opens PR via workflow (this script only writes the file).
"""

from __future__ import annotations
import os, sys
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
TOC_FILE = ROOT / "Table Of Contents.md"   # keep your existing filename

# ------- Tunables -------
EXCLUDE_DIRS = {
    ".git", "__pycache__", ".mypy_cache", ".pytest_cache",
    ".venv", "venv", "node_modules", "dist", "build", ".idea", ".vscode"
}
EXCLUDE_FILES = {".DS_Store"}

# Show files with these suffixes (set to None to show all)
ALLOW_EXTS = {".md", ".py", ".ipynb", ".yml", ".yaml", ".toml"}  # tweak as you like

MAX_DEPTH = 2            # 0 = just top-level; 2 = include grandchildren
MAX_ITEMS_PER_DIR = 100  # cap long folders
FOLDERS_FIRST = True
# Optional hand-written descriptions you want to keep
DESCRIPTIONS = {
    # "Abo
