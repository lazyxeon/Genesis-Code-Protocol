<<<<<< codex/analyze-failing-github-workflows
"""Validate workflow manifest schema."""
import json
from pathlib import Path


def test_manifest_has_required_fields() -> None:
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["id"] == "bwb::ci-workflow-diagnoser::v1"
    assert data["security"]["supply_chain"]["sbom"] is True
=======
import json

def test_manifest_has_required_fields():
    with open("workflow_manifest.json") as f:
        manifest = json.load(f)
    assert manifest["version"] == "1.0.0"
    assert manifest["steps"]
>>>>>> main
