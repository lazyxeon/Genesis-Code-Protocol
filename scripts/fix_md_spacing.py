#!/usr/bin/env python3
"""Utility to normalize spacing in Markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
LIST_RE = re.compile(r"^(\s*)([-*+]|[0-9]+\.)\s+")


def _blank(line: str) -> bool:
    """Return True if the given line is blank."""
    return line.strip() == ""


def _emit_heading(out: list[str], line: str, next_line: str) -> None:
    """Append a heading and ensure surrounding blank lines."""
    if out and not _blank(out[-1]):
        out.append("\n")
    out.append(line)
    if not _blank(next_line):
        out.append("\n")


def _emit_list_block(lines: list[str], start: int, out: list[str]) -> int:
    """Append a contiguous Markdown list block starting at ``start``."""
    i = start
    n = len(lines)
    while i < n and LIST_RE.match(lines[i]) and not lines[i].lstrip().startswith("```"):
        out.append(lines[i])
        i += 1
    return i


def normalize_spacing(lines: list[str]) -> list[str]:
    """Enforce markdownlint-friendly spacing around headings and lists."""
    out: list[str] = []
    in_code = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        if line.lstrip().startswith("```"):
            out.append(line)
            in_code = not in_code
            i += 1
            continue

        if not in_code and HEADING_RE.match(line):
            next_line = lines[i + 1] if i + 1 < n else ""
            _emit_heading(out, line, next_line)
            i += 1
            continue

        if not in_code and LIST_RE.match(line):
            prev_nonblank = next(
                (out[j] for j in range(len(out) - 1, -1, -1) if not _blank(out[j])),
                None,
            )
            if prev_nonblank is None or not LIST_RE.match(prev_nonblank):
                if out and not _blank(out[-1]):
                    out.append("\n")
            i = _emit_list_block(lines, i, out)
            next_line = lines[i] if i < n else ""
            if not _blank(next_line):
                out.append("\n")
            continue

        out.append(line)
        i += 1

    compact: list[str] = []
    for line in out:
        if not (compact and compact[-1] == "\n" and line == "\n"):
            compact.append(line)
    return compact


def main() -> None:
    """CLI entry point for normalizing Markdown spacing."""
    if len(sys.argv) != 2:
        print("Usage: fix_md_spacing.py <markdown-file>")
        sys.exit(2)

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8").splitlines(keepends=True)
    fixed = normalize_spacing(text)
    if fixed != text:
        path.write_text("".join(fixed), encoding="utf-8")
        print(f"Normalized spacing in {path}")
    else:
        print(f"No changes needed for {path}")


if __name__ == "__main__":
    main()
