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
