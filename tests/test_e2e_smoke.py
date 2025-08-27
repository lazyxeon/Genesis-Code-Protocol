"""End-to-end smoke test."""
import json
from pathlib import Path
from src.ingest import main


def test_ingest_creates_output(tmp_path) -> None:
    input_path = tmp_path / "in.json"
    output_path = tmp_path / "out.json"
    input_path.write_text(json.dumps({"records": [1, 2]}))
    main(str(input_path), str(output_path))
    data = json.loads(output_path.read_text())
    assert data["records"] == [1, 2]
