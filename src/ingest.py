<<<<<< codex/analyze-failing-github-workflows
"""Ingest step for ci-workflow-diagnoser."""
from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from time import time

from .utils import atomic_write

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def main(input_path: str, output_path: str) -> None:
    """Load records from ``input_path`` and persist them to ``output_path``."""
    start = time()
    data = json.loads(Path(input_path).read_text())
    logging.info("records_ingested=%d", len(data.get("records", [])))
    atomic_write(Path(output_path), json.dumps({"records": data.get("records", [])}))
    logging.info("duration_ms=%d", int((time() - start) * 1000))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest workflow logs")
    parser.add_argument("--input", required=True, help="Path to JSON input file")
    parser.add_argument("--output", required=True, help="Path to write normalized output")
    args = parser.parse_args()
    main(args.input, args.output)
=======
from .config import Config
from .logging_utils import log


def main(cfg: Config | None = None) -> bytes:
    cfg = cfg or Config()
    log("ingest.start", source=cfg.source_archive)
    data = b"dummy"
    log("ingest.complete", size=len(data))
    return data
>>>>>> main
