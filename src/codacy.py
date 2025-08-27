from __future__ import annotations

import os
from typing import Dict

from .utils import get_logger

logger = get_logger(__name__)


def main() -> Dict[str, str]:
    """Simulate running Codacy scan."""
    if not os.getenv("CODACY_PROJECT_TOKEN"):
        logger.info("codacy skipped: missing CODACY_PROJECT_TOKEN")
        return {"status": "skipped"}
    logger.info("codacy started")
    return {"status": "ok"}


if __name__ == "__main__":  # pragma: no cover - script mode
    main()
