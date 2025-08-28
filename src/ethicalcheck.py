from __future__ import annotations

import os

from .utils import get_logger

logger = get_logger(__name__)


def main() -> dict[str, str]:
    """Simulate running EthicalCheck scan."""
    if not os.getenv("ETHICALCHECK_OAS_URL") or not os.getenv("ETHICALCHECK_EMAIL"):
        return {"status": "skipped"}
    logger.info("ethicalcheck started")
    return {"status": "ok"}
