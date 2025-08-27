<<<<<< codex/analyze-failing-github-workflows
"""Rollback behavior on failure."""
from pathlib import Path
import pytest
from src.ingest import main


def test_failed_ingest_keeps_original_output(tmp_path) -> None:
    input_path = tmp_path / "bad.json"
    output_path = tmp_path / "out.json"
    output_path.write_text("old")
    input_path.write_text("{")
    with pytest.raises(Exception):
        main(str(input_path), str(output_path))
    assert output_path.read_text() == "old"
=======
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import rollback

def test_rollback_called(caplog):
    caplog.set_level("INFO")
    try:
        rollback.apply()
        raise rollback.RemediationError("fail")
    except rollback.RemediationError:
        rollback.rollback()
    assert any("rolling back" in m for m in caplog.text.splitlines())
>>>>>> main
