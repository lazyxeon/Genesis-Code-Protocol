import json

from src import remediate, scan


def test_smoke(tmp_path) -> None:
    report_file = tmp_path / "report.json"
    scan.scan_repository("owner/repo")
    report_file.write_text(json.dumps({"critical": 0}))
    pr = remediate.remediate({"critical": 0})
    assert pr.startswith("https://")
