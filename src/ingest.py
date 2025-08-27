"""Ingest step: normalize input records."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from time import time

from .logging_utils import get_logger
from .errors import RetryableError

log = get_logger(__name__)

def main(input_path: str, output_path: str) -> None:
    start = time()
    path = Path(input_path)
    if not path.exists():
        raise RetryableError(f"missing input {input_path}")
    data = json.loads(path.read_text())
    records = data.get("records", [])
    Path(output_path).write_text(json.dumps({"records": records}))
    log.info("records_ingested=%d duration_ms=%d", len(records), int((time()-start)*1000))

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.input, args.output)
