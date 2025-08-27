"""Performance probe."""

import time

from src.scan import scan_repository


def test_scan_perf() -> None:
    """Ensure repository scan stays within latency budget."""
    start = time.time()
    scan_repository("owner/repo")
    assert (time.time() - start) < 0.5
