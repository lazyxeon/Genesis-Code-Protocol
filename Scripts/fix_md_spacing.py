#!/usr/bin/env python3
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r'^(#{1,6})\s+\S')
LIST_RE = re.compile(r'^(\s*)([-*+]|[0-9]+\.)\s+')

def normalize_spacing(lines):
    """
    Enforce markdownlint-friendly spacing:
      - MD022: one blank line above/below headings
      - MD032: blank line before/after list blocks
    Skips code fences (```).
    """
    out = []
    in_code = False

    def blank(line): return line.strip() == ""

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        # Track fenced code blocks; don't touch spacing inside them
        if line.lstrip().startswith("```"):
            out.append(line)
            in_code = not in_code
            i += 1
            continue

        if not in_code:
            # Headings: ensure blank line before and after
            if HEADING_RE.match(line):
                # Ensure one blank line before (if not start of file and not already blank)
                if len(out) > 0 and not blank(out[-1]):
                    out.append("\n")
                out.append(line)
                # Ensure one blank line after (if not already blank or end)
                next_line = lines[i+1] if i + 1 < n else ""
                if not blank(next_line):
                    out.append("\n")
                i += 1
                continue

            # Lists: ensure blank line before the start of a list-block and after its end
            if LIST_RE.match(line):
                # If previous non-blank line wasn't a list item, insert blank line
                prev_nonblank = None
                for j in range(len(out) - 1, -1, -1):
                    if not blank(out[j]):
                        prev_nonblank = out[j]
                        break
                if prev_nonblank is None or not LIST_RE.match(prev_nonblank):
                    if len(out) > 0 and not blank(out[-1]):
                        out.append("\n")

                # Emit the whole contiguous list block
                while i < n and LIST_RE.match(lines[i]) and not lines[i].lstrip().startswith("```"):
                    out.append(lines[i])
                    i += 1

                # Ensure a blank line after the list block (unless EOF or already blank)
                next_line = lines[i] if i < n else ""
                if not blank(next_line):
                    out.append("\n")
                continue

        # Default: pass through
        out.append(line)
        i += 1

    # Collapse consecutive blank lines to a single blank line
    compact = []
    for l in out:
        if not (compact and compact[-1] == "\n" and l == "\n"):
            compact.append(l)
    return compact

def main():
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
