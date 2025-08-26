#!/usr/bin/env bash
# Quick audit to find likely unpinned actions inside .github/workflows
set -euo pipefail
echo "Scanning .github/workflows for 'uses:' lines that look unpinned..."
grep -R --line-number "^\\s*uses: .*@" .github/workflows || true
echo
echo "Any 'uses: owner/repo@v1' or 'uses: owner/repo@main' should be reviewed and replaced with a pinned commit SHA for stronger supply-chain integrity."
