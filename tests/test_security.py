"""Security checks."""
import json
import logging
from pathlib import Path
from src.ingest import main


def test_no_secret_in_logs(tmp_path, caplog) -> None:
    caplog.set_level(logging.INFO)
    input_path = tmp_path / "in.json"
    output_path = tmp_path / "out.json"
    input_path.write_text(json.dumps({"records": []}))
    main(str(input_path), str(output_path))
    for record in caplog.records:
        assert "CI_WORKFLOW_DIAGNOSER_TOKEN" not in record.message
