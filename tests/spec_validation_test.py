import json
from pathlib import Path


def test_manifest_has_required_fields():
    manifest = json.loads(Path("workflow_manifest.json").read_text())
    for field in ["id", "steps", "SLOs"]:
        assert field in manifest
    assert len(manifest["steps"]) == 3
