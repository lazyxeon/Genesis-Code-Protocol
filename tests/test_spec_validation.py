import json


def test_manifest_has_required_fields() -> None:
    with open("workflow_manifest.json") as f:
        manifest = json.load(f)
    assert manifest["version"] == "1.0.0"
    assert manifest["steps"]
