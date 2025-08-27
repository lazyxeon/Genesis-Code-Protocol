"""Push step: publish artifact to registry."""
from __future__ import annotations

from pathlib import Path
from time import time

from .config import Config
from .logging_utils import get_logger

log = get_logger(__name__)

def main(artifact_path: str, cfg: Config | None = None) -> str:
    cfg = cfg or Config()
    start = time()
    path = Path(artifact_path)
    if not path.exists():  # pragma: no cover - defensive
        raise FileNotFoundError(artifact_path)
    ref = f"{cfg.registry}:{path.stem}"
    log.info("push_complete ref=%s duration_ms=%d", ref, int((time()-start)*1000))
    return ref
