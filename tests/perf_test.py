"""Performance probe."""

import time

from src import main


def test_scan_perf(tmp_path, monkeypatch) -> None:
    """Ensure workflow run stays within latency budget."""
    report_path = tmp_path / "r.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    start = time.perf_counter()
    main.run()
    assert (time.perf_counter() - start) < 1.0
