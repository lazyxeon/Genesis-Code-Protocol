.RECIPEPREFIX := >
.PHONY: install test build sbom sign package ingest

install:
>pip install -r requirements.txt

test:
>pytest -q

build:
>mkdir -p dist
>echo '{"records": []}' > sample.json
>python -m src.ingest --input sample.json --output dist/report.json

sbom:
>syft . -o json > sbom.json

sign:
>cosign sign-blob --key $$COSIGN_KEY sbom.json

package: build sbom
>zip -r dist/ci-workflow-diagnoser-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md docs/ci-workflow-diagnoser-runbook.md sbom.json

ingest:
>python -m src.ingest --input sample.json --output dist/report.json
