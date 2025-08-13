#!/usr/bin/env python3
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

EXCLUDE_DIRS = {
    ".git", ".github", "__pycache__", ".mypy_cache", ".pytest_cache",
    ".venv", "venv", "node_modules", "dist", "build", ".idea", ".vscode"
}
EXCLUDE_FILES = {".DS_Store"}

MAX_DEPTH = 2          # change to 3+ if you want deeper trees
MAX_ENTRIES = 200      # safety cap per dir

BEGIN = "<!-- BEGIN REPO TREE -->"
END = "<!-- END REPO TREE -->"

def build_tree(root: Path, prefix: str = "", depth: int = 0) -> str:
    if depth > MAX_DEPTH:
        return ""
    try:
        names = sorted(os.listdir(root))[:MAX_ENTRIES]
    except PermissionError:
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
            lines.append(build_tree(p, prefix + "├─ ", depth + 1))
        else:
            lines.append(f"{prefix}{name}")
    return "\n".join(l for l in lines if l)

def replace_between(text: str, start: str, end: str, new_block: str) -> str:
    pat = re.compile(rf"({re.escape(start)})(.*?){re.escape(end)}", re.DOTALL)
    repl = f"{start}\n```\n{new_block}\n```\n{end}"
    return pat.sub(repl, text, count=1) if pat.search(text) else text + "\n\n" + repl + "\n"

def main():
    tree = build_tree(ROOT) or "(empty)"
    content = README.read_text(encoding="utf-8")
    updated = replace_between(content, BEGIN, END, tree)
    if updated != content:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated with repository tree.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
