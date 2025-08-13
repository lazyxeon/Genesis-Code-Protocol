#!/usr/bin/env python3
import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

# Tweak as needed
EXCLUDE_DIRS = {
    ".git", ".github", "__pycache__", ".mypy_cache", ".pytest_cache",
    ".venv", "venv", "node_modules", "dist", "build", ".idea", ".vscode"
}
EXCLUDE_FILES = {".DS_Store"}

MAX_DEPTH = 2          # increase to 3+ if you want deeper trees
MAX_ENTRIES = 500      # safety cap per directory

BEGIN = "<!-- BEGIN REPO TREE -->"
END = "<!-- END REPO TREE -->"

def build_tree(root: Path, prefix: str = "", depth: int = 0) -> str:
    """Return a markdown-ish tree listing of files/dirs under root."""
    if depth > MAX_DEPTH:
        return ""
    try:
        names = sorted(os.listdir(root))[:MAX_ENTRIES]
    except Exception:
        return ""
    lines = []
    for name in names:
        if name in EXCLUDE_FILES:
            continue
        p = root / name
        if p.is_dir():
            if name in EXCLUDE_DIRS:
                continue
            lines.append(f"{prefix}{name}/")
            subtree = build_tree(p, prefix + "├─ ", depth + 1)
            if subtree:
                lines.append(subtree)
        else:
            lines.append(f"{prefix}{name}")
    return "\n".join(l for l in lines if l)

def replace_between(text: str, start: str, end: str, new_block: str) -> str:
    pat = re.compile(rf"({re.escape(start)})(.*?){re.escape(end)}", re.DOTALL)
    repl = f"{start}\n```\n{new_block}\n```\n{end}"
    if pat.search(text):
        return pat.sub(repl, text, count=1)
    # If markers missing, append a section at the end
    extra = f"\n\n## Repository Structure (auto-generated)\n\n{repl}\n"
    return text + extra

def main():
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
