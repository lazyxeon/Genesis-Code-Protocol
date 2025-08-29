from __future__ import annotations

from pathlib import Path

from .utils import get_logger

logger = get_logger(__name__)


class RemediationError(Exception):
    """Raised when remediation fails."""


def apply() -> None:
    logger.info("applying changes")


def rollback() -> None:
    logger.info("rolling back changes")


def perform(reason: str) -> None:
    """Record rollback action and persist reason to file."""
    logger.error("rollback: %s", reason)
    Path("rollback.log").write_text(reason)


if __name__ == "__main__":
    try:
        apply()
        raise RemediationError("simulated failure")
    except RemediationError as exc:
        perform(str(exc))
        rollback()
