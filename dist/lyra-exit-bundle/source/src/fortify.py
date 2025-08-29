from __future__ import annotations

import os
from typing import Dict

from .utils import get_logger

logger = get_logger(__name__)


REQUIRED = [
    "FOD_TENANT",
    "FOD_USER",
    "FOD_PAT",
    "SSC_TOKEN",
    "SC_CLIENT_AUTH_TOKEN",
    "DEBRICKED_TOKEN",
]


def main() -> Dict[str, str]:
    """Simulate running Fortify scan."""
    missing = [k for k in REQUIRED if not os.getenv(k)]
    if missing:
        logger.info("fortify skipped: missing %s", ",".join(missing))
        return {"status": "skipped"}
    logger.info("fortify started")
    return {"status": "ok"}


if __name__ == "__main__":  # pragma: no cover - script mode
    main()
