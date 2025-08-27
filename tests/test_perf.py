import time

from src.scan import scan_repository


def test_scan_perf() -> None:
    start = time.time()
    scan_repository("owner/repo")
    assert (time.time() - start) < 0.5
