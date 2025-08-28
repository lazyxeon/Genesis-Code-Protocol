import json
import logging
import sys

logger = logging.getLogger("fuzzing_vuln_scan")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def log(event: str, **fields) -> None:
    """Emit a structured log line."""
    data = {"event": event, **fields}
    logger.info(json.dumps(data))
