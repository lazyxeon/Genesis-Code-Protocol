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
