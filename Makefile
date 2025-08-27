.PHONY: install test build sbom package

install:
pip install -r requirements.txt

test:
pytest -q

build:
docker build -t secure-repo-workflow .

sbom:
syft . -o json > sbom.json

package:
zip -r dist/secure-repo-scorecard-remediation-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md docs/runbook.md tests src
