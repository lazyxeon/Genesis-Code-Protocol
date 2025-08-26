#!/usr/bin/env bash
# Simple audit script to find uses: lines in .github/workflows and flag likely unpinned actions (tags like @v, @main, @latest).
set -euo pipefail
echo "Scanning .github/workflows for unpinned action references..."
grep -R --line-number "uses: .*@" .github/workflows || true
echo
echo "Recommend: replace floating tags (e.g. @v1, @v2, @main, @latest) with pinned commit SHAs (e.g. @<full-40-char-sha>) for supply-chain integrity."
