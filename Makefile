.RECIPEPREFIX := >
.PHONY: install lint test build sbom sign package canary

install:
>pip install -r requirements.txt

lint:
>pre-commit run --all-files

test:
>pytest -q

build:
>docker build -t security-scan-workflow .

sbom:
>syft . -o json > sbom.json

sign:
>cosign sign-blob --key $$COSIGN_KEY sbom.json

package: build sbom
>mkdir -p dist
>zip -r dist/security-scan-workflow-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md src tests Makefile

canary:
>echo "Launching canary deployment"
