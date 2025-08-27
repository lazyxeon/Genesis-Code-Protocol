"""Validate workflow manifest schema."""

import json
from pathlib import Path


def test_manifest_has_required_fields() -> None:
    """Ensure critical keys exist in the manifest."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    for key in ["id", "version", "steps", "SLOs", "security", "artifact_plan"]:
        assert key in data
    assert data["security"]["supply_chain"]["sbom"] is True
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"
