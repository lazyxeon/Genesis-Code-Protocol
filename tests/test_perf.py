import time
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src.scan import scan_repository

def test_scan_perf():
    start = time.time()
    scan_repository("owner/repo")
    assert (time.time() - start) < 0.5
