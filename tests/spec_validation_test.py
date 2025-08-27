"""Validate workflow manifest schema."""
import json
from pathlib import Path

def test_manifest_has_required_fields() -> None:
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["id"] == "bwb::build-pipeline-stabilizer::v1"
    assert data["security"]["supply_chain"]["sbom"] is True
