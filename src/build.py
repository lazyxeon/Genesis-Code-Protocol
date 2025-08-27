"""Build step: compile sources into an artifact."""
from __future__ import annotations

from pathlib import Path
from time import time

from .logging_utils import get_logger

log = get_logger(__name__)

def main(source_dir: str, artifact_path: str) -> Path:
    start = time()
    artifact = Path(artifact_path)
    artifact.write_text("artifact")
    log.info("build_complete path=%s duration_ms=%d", artifact, int((time()-start)*1000))
    return artifact
