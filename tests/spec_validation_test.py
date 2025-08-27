import json
from pathlib import Path


def test_manifest_has_required_fields():
    data = json.loads(Path("workflow_manifest.json").read_text())
    for key in ["id", "steps", "security", "artifact_plan"]:
        assert key in data
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"
