#!/usr/bin/env bash
set -euo pipefail

echo "[validate_precommit] Phase 1 (format/hygiene auto-fix)"
SKIP=ruff-lint,mypy-report,check-large-files,check-yaml pre-commit run --all-files || true

if ! git diff --quiet; then
  echo "[validate_precommit] Auto-fix changes detected. Commit them before proceeding." >&2
  git --no-pager diff --name-only
  exit 1
fi

echo "[validate_precommit] Phase 2 (enforcement)"
SKIP=ruff-format pre-commit run --all-files --show-diff-on-failure

echo "[validate_precommit] Phase 3 (mypy advisory)"
mypy || true

echo "[validate_precommit] Complete."
