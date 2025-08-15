#!/usr/bin/env python3
import json, re, sys
if len(sys.argv) < 2:
    print("usage: modulift_explain.py <rules.json>", file=sys.stderr)
    sys.exit(2)
rules = json.load(open(sys.argv[1]))
log = sys.stdin.read()
for r in rules:
    m = re.search(r["match"], log, re.S)
    if m:
        hint = r["hint"]
        for i, g in enumerate(m.groups(), start=1):
            hint = hint.replace(f"${i}", g)
        print("→", hint)
