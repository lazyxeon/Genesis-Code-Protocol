<<<<<< codex/analyze-failing-github-workflows
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
=======
import io
import logging
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src.utils import get_logger


def test_no_secret_in_logs(monkeypatch):
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger = get_logger("test")
    logger.handlers = [handler]
    logger.info("hello")
    assert "SECURE_REPO_TOKEN" not in stream.getvalue()
>>>>>> main
