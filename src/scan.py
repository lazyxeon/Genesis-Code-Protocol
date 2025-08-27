from .config import Config
from .logging_utils import log


def main(data: bytes, cfg: Config | None = None) -> dict:
    cfg = cfg or Config()
    log("scan.start")
    findings = {"vulnerabilities": []}
    log("scan.complete", vulnerabilities=len(findings["vulnerabilities"]))
    return findings
