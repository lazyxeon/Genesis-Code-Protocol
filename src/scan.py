from typing import Dict, List, Optional

from .config import Config
from .logging_utils import log


def main(data: bytes, cfg: Optional[Config] = None) -> Dict[str, List[str]]:
    cfg = cfg or Config()
    log("scan.start")
    findings: Dict[str, List[str]] = {"vulnerabilities": []}
    log("scan.complete", vulnerabilities=len(findings["vulnerabilities"]))
    return findings


def scan_repository(repo: str) -> Dict[str, int]:
    """Simulate a scorecard scan returning counts of findings."""
    log("scan.repo", repo=repo)
    return {"critical": 0, "high": 1, "medium": 2, "low": 0}
