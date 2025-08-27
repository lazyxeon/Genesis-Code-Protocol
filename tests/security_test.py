import json

def test_secrets_declared():
    with open('workflow_manifest.json') as f:
        manifest = json.load(f)
    assert 'ENV:PYPI_TOKEN' in manifest['security']['secrets']
