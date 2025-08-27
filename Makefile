.RECIPEPREFIX := >
.PHONY: install test build sbom sign package

install:
>pip install -r requirements.txt

test:
>pytest -q

build:
>mkdir -p dist
>echo '{"records": []}' > sample.json
>python -m src.ingest --input sample.json --output dist/normalized.json
>python -m src.build . dist/artifact.txt

sbom:
>syft . -o json > sbom.json

sign:
>cosign sign-blob --key $$COSIGN_KEY sbom.json

package: build sbom
>zip -r dist/build-pipeline-stabilizer-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md tests sbom.json docs/runbook.md
