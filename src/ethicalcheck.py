from __future__ import annotations

import os
from typing import Dict

from .utils import get_logger

logger = get_logger(__name__)


def main() -> Dict[str, str]:
    """Simulate running EthicalCheck scan."""
    if not os.getenv("ETHICALCHECK_OAS_URL") or not os.getenv("ETHICALCHECK_EMAIL"):
        logger.info(
            "ethicalcheck skipped: missing ETHICALCHECK_OAS_URL or ETHICALCHECK_EMAIL"
        )
        return {"status": "skipped"}
    logger.info("ethicalcheck started")
    return {"status": "ok"}


if __name__ == "__main__":  # pragma: no cover - script mode
    main()
