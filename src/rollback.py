class RemediationError(Exception):
    """Raised when remediation fails."""


def apply() -> None:
    import logging

    logging.getLogger(__name__).info("applying changes")


def rollback() -> None:
    import logging

    logging.getLogger(__name__).info("rolling back changes")


def perform(reason: str) -> None:
    import logging
    from pathlib import Path

    logging.getLogger(__name__).error("rollback due to %s", reason)
    Path("rollback.log").write_text(reason)


if __name__ == "__main__":
    try:
        apply()
        raise RemediationError("simulated failure")
    except RemediationError:
        rollback()
