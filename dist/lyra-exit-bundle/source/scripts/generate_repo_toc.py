#!/usr/bin/env python3
"""Generate a markdown table of contents for the repository."""

# -*- coding: utf-8 -*-

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Table Of Contents.md"

IGNORE_DIRS = {
    ".git",
    ".github",
    ".devcontainer",
    "docker",
    "__pycache__",
    ".venv",
}
IGNORE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".ipynb"}


def rel(p: Path) -> str:
    """Return path ``p`` relative to repo root with POSIX separators."""
    return str(p.relative_to(ROOT)).replace("\\", "/")


def should_list(p: Path) -> bool:
    """Decide whether ``p`` should appear in the generated listing."""
    if p.is_dir():
        return p.name not in IGNORE_DIRS
    ext = p.suffix.lower()
    return ext not in IGNORE_EXTS


def main() -> None:
    """Write the repository structure to ``Table Of Contents.md``."""
    try:
        if not ROOT.exists():
            raise FileNotFoundError(f"Repository root not found: {ROOT}")
            
        entries: list[str] = ["# Repository Structure", ""]
        
        for base, dirs, files in os.walk(ROOT):
            try:
                dirs[:] = [d for d in dirs if should_list(Path(base) / d)]
                level = Path(base).relative_to(ROOT).parts
                if level:
                    entries.append(f"{'  ' * (len(level)-1)}- **{Path(base).name}/**")
                indent = "  " * len(level)
                for f in sorted(files):
                    p = Path(base) / f
                    if should_list(p):
                        entries.append(f"{indent}- {rel(p)}")
            except (OSError, PermissionError) as e:
                print(f"Warning: Skipping {base} due to error: {e}")
                continue
                
        if len(entries) <= 2:  # Only header and empty line
            raise RuntimeError("No files found to include in table of contents")
            
        OUT.write_text("\n".join(entries) + "\n", encoding="utf-8")
        print(f"Wrote {rel(OUT)}")
        
    except Exception as e:
        print(f"Error generating table of contents: {e}")
        raise


if __name__ == "__main__":
    main()
