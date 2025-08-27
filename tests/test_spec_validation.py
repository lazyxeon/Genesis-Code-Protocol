import json

def test_manifest_has_required_fields():
    with open("workflow_manifest.json") as f:
        manifest = json.load(f)
    assert manifest["version"] == "1.0.0"
    assert manifest["steps"]
