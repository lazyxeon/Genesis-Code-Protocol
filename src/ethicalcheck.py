from __future__ import annotations

import os
from typing import Dict

from .utils import get_logger

logger = get_logger(__name__)


def main() -> Dict[str, str]:
    """Simulate running EthicalCheck scan."""
    required = ("ETHICALCHECK_OAS_URL", "ETHICALCHECK_EMAIL")
    if not all(os.getenv(var) for var in required):
        logger.info("ethicalcheck skipped: missing %s", " or ".join(required))
        return {"status": "skipped"}
    logger.info("ethicalcheck started")
    return {"status": "ok"}


if __name__ == "__main__":  # pragma: no cover - script mode
    main()
