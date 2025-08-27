from typing import Optional

from .config import Config
from .logging_utils import log


def main(cfg: Optional[Config] = None) -> bytes:
    cfg = cfg or Config()
    log("ingest.start", source=cfg.source_archive)
    data = b"dummy"
    log("ingest.complete", size=len(data))
    return data
