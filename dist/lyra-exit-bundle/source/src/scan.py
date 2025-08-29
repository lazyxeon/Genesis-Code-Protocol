from typing import Dict, List, Optional

from .config import Config
from .logging_utils import log


def main(data: bytes, cfg: Optional[Config] = None) -> Dict[str, List[str]]:
    cfg = cfg or Config()
    log("scan.start")
    findings: Dict[str, List[str]] = {"unstable_workflows": []}
    log("scan.complete", unstable=len(findings["unstable_workflows"]))
    return findings


def scan_repository(repo: str) -> Dict[str, int]:
    """Simulate checking workflow runs and returning counts of failures."""
    log("scan.repo", repo=repo)
    return {"failures": 0, "success": 1}
