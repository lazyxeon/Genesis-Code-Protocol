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
