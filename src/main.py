"""Entrypoint wiring all steps for manual runs."""
from __future__ import annotations

import argparse
from pathlib import Path

from . import build, ingest, push, rollback


def run_pipeline(source: str, workdir: str) -> str:
    work = Path(workdir)
    work.mkdir(parents=True, exist_ok=True)
    normalized = work / "normalized.json"
    ingest.main(source, str(normalized))
    artifact = work / "artifact.txt"
    build.main(str(work), str(artifact))
    return push.main(str(artifact))


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--workdir", required=True)
    args = parser.parse_args()
    try:
        ref = run_pipeline(args.input, args.workdir)
        print(ref)
    except Exception as exc:  # noqa: BLE001
        rollback.main(type(exc).__name__)
        raise
