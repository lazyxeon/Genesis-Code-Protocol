#!/usr/bin/env bash
# Quick audit to find likely unpinned actions inside .github/workflows.
# SHA-pinned actions are ignored by this audit.
set -euo pipefail
echo "Scanning .github/workflows for actions using loose refs (tags like 'v*', 'main', or 'master')..."
grep -R --line-number -E "^\\s*uses: .+@(v[0-9]+|main|master)$" .github/workflows || true
echo
echo "Any 'uses: owner/repo@v1', 'uses: owner/repo@main', or 'uses: owner/repo@master' should be reviewed and replaced with a pinned commit SHA for stronger supply-chain integrity."
