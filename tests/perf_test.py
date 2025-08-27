"""Performance probe for ingest step."""
import json
import time
from pathlib import Path

from src.ingest import main

def test_ingest_latency(tmp_path):
    sample = tmp_path / "s.json"
    sample.write_text(json.dumps({"records": list(range(100))}))
    out = tmp_path / "o.json"
    start = time.time()
    main(str(sample), str(out))
    assert (time.time() - start) * 1000 < 1200
