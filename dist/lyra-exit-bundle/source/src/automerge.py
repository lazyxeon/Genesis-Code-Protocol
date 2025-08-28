from __future__ import annotations

import os
from typing import Any, Dict

from .utils import get_logger

logger = get_logger(__name__)


class AutoMergeError(Exception):
    """Raised when auto-merge cannot be enabled."""


def enable_automerge(pr_number: int, repo: str, token: str | None) -> Dict[str, Any]:
    """Enable auto-merge for a PR.

    Returns a status dictionary; if token is missing the step is skipped.
    """
    if not token:
        logger.info("automerge skipped: missing token")
        return {"status": "skipped"}

    logger.info("automerge enabled", extra={"pr": pr_number, "repo": repo})
    # In this skeleton we do not call the GitHub API.
    return {"status": "enabled", "pr": pr_number, "repo": repo}


def main() -> Dict[str, Any]:
    """Entrypoint used by the workflow step."""
    pr = int(os.getenv("PR_NUMBER", "0"))
    repo = os.getenv("REPO", "")
    token = os.getenv("GITHUB_TOKEN")
    return enable_automerge(pr, repo, token)


if __name__ == "__main__":
    print(main())
