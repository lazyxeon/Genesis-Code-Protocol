from __future__ import annotations

from typing import Dict

from .config import Config
from .logging_utils import log


def main(data: bytes, cfg: Config | None = None) -> dict[str, list[str]]:
    cfg = cfg or Config()
    log("scan.start")
    findings: dict[str, list[str]] = {"vulnerabilities": []}
    log("scan.complete", vulnerabilities=len(findings["vulnerabilities"]))
    return findings


def scan_repository(repo: str) -> Dict[str, int]:
    """Simulate a scorecard scan returning counts of findings."""
    log("scan.repo", repo=repo)
    return {"critical": 0, "high": 1, "medium": 2, "low": 0}
