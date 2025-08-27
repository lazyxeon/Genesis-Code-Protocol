import json

def test_manifest_has_required_fields():
    with open('workflow_manifest.json') as f:
        data = json.load(f)
    assert data['id'] == 'bwb::matrix-ci-repair::v1'
    assert data['operational_env'] == 'container'
    assert 'steps' in data and len(data['steps']) == 3
