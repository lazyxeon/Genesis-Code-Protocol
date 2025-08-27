from pathlib import Path

from .logging_utils import log


def perform(reason: str) -> None:
    """Record rollback action."""
    log("rollback", reason=reason)
    Path("rollback.log").write_text(reason)
