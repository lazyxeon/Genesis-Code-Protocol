<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
from pathlib import Path

from .logging_utils import log


def perform(reason: str) -> None:
    """Record rollback action."""
    log("rollback", reason=reason)
    Path("rollback.log").write_text(reason)
=======
from __future__ import annotations
import logging

from .utils import get_logger

logger = get_logger(__name__)

class RemediationError(Exception):
    """Raised when remediation fails."""


def apply() -> None:
    logger.info("applying changes")


def rollback() -> None:
    logger.info("rolling back changes")

if __name__ == "__main__":
    try:
        apply()
        raise RemediationError("simulated failure")
    except RemediationError:
        rollback()
>>>>>> main
