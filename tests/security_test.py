"""Security checks for manifest."""
import json

def test_manifest_secrets() -> None:
    data = json.loads(open("workflow_manifest.json").read())
    assert "ENV:REGISTRY_TOKEN" in data["security"]["secrets"]
