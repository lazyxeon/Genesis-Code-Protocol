import json
from pathlib import Path


def test_manifest_has_required_fields():
<<<<<< codex/develop-and-implement-matrix-ci
    manifest = json.loads(Path("workflow_manifest.json").read_text())
    for field in ["id", "steps", "SLOs"]:
        assert field in manifest
    assert len(manifest["steps"]) == 3
=======
    data = json.loads(Path("workflow_manifest.json").read_text())
    for key in ["id", "steps", "security", "artifact_plan"]:
        assert key in data
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"
>>>>>> main
