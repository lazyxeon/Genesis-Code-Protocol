#!/usr/bin/env bash
# Simple grep for uses:@... without a SHA (quick audit)
set -e
echo "Scanning workflows for unpinned actions (tags instead of SHAs)..."
grep -R --line-number "uses: .*@" .github/workflows || true
echo "Review results and replace tags (e.g. v1) with pinned commit SHAs for higher Scorecard trust."
