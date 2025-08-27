from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Dict

from .config import Config
from .logging_utils import log
from .utils import get_logger

logger = get_logger(__name__)


def scan_repository(repo: str) -> Dict[str, int]:
    """Simulate a scorecard scan returning counts of findings."""
    logger.info("scanning repository %s", repo)
    time.sleep(0.01)
    return {"critical": 0, "high": 1, "medium": 2, "low": 0}


def main(
    data: bytes | None = None, cfg: Config | None = None
) -> dict[str, list[dict[str, str]]]:
    cfg = cfg or Config()
    log("scan.start")
    findings: dict[str, list[dict[str, str]]] = {"vulnerabilities": []}
    log("scan.complete", vulnerabilities=len(findings["vulnerabilities"]))
    return findings


def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--output", default="scorecard_report.json")
    args = parser.parse_args()
    report = scan_repository(args.repo)
    Path(args.output).write_text(json.dumps(report))
    logger.info("wrote %s", args.output)


if __name__ == "__main__":
    cli()
