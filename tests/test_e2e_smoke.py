<<<<<< codex/analyze-failing-github-workflows
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
=======
from pathlib import Path
import json
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import scan, remediate

def test_smoke(tmp_path, monkeypatch):
    report_file = tmp_path / "report.json"
    scan.scan_repository("owner/repo")
    report_file.write_text(json.dumps({"critical":0}))
    pr = remediate.remediate({"critical":0})
    assert pr.startswith("https://")
>>>>>> main
