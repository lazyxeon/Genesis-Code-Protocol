"""End-to-end smoke test for pipeline."""
import json
from pathlib import Path

from src import build, ingest, push

def test_e2e(tmp_path):
    sample = tmp_path / "in.json"
    sample.write_text(json.dumps({"records": [1]}))
    out = tmp_path / "out.json"
    ingest.main(str(sample), str(out))
    artifact = tmp_path / "artifact.txt"
    build.main(str(tmp_path), str(artifact))
    ref = push.main(str(artifact))
    assert out.exists()
    assert ref.endswith("artifact")
