"""Validate workflow manifest schema."""

import json
from pathlib import Path


def test_manifest_has_required_fields() -> None:
    """Ensure critical keys exist in the manifest."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    for key in ["id", "version", "steps", "SLOs", "security", "artifact_plan"]:
        assert key in data
    assert data["id"] == "bwb::dependabot-automerge::v1"
    assert data["security"]["supply_chain"]["sbom"] is True
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"


def test_manifest_has_pr_number_input() -> None:
    """Ensure pr_number input is declared."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert any(i["name"] == "pr_number" for i in data["inputs"])
