<<<<<< codex/analyze-failing-github-workflows
"""Performance probe."""
import json
import time
from pathlib import Path
from src.ingest import main


def test_ingest_under_latency_budget(tmp_path) -> None:
    input_path = tmp_path / "in.json"
    output_path = tmp_path / "out.json"
    input_path.write_text(json.dumps({"records": list(range(100))}))
    start = time.time()
    main(str(input_path), str(output_path))
    assert (time.time() - start) * 1000 < 1200
=======
import time
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src.scan import scan_repository

def test_scan_perf():
    start = time.time()
    scan_repository("owner/repo")
    assert (time.time() - start) < 0.5
>>>>>> main
