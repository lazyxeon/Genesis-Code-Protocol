import json
from pathlib import Path
from typing import Optional

from .config import Config
from .logging_utils import log


def main(findings: dict, cfg: Optional[Config] = None) -> str:
    cfg = cfg or Config()
    log("report.start")
    path = Path(cfg.report_path)
    path.write_text(json.dumps(findings))
    log("report.complete", path=str(path))
    return str(path)
