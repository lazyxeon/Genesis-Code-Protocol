.RECIPEPREFIX := >
.PHONY: install lint test build sbom sign package canary

install:
>pip install -r requirements.txt

lint:
>pre-commit run --all-files

test:
>pytest -q

build:
>if command -v docker >/dev/null 2>&1; then docker build -t dependabot-automerge-workflow .; else echo "docker not installed, skipping container build"; fi

sbom:
>if command -v syft >/dev/null 2>&1; then syft . -o json > sbom.json; else python scripts/generate_sbom.py sbom.json; fi

sign:
>cosign sign-blob --key $$COSIGN_KEY sbom.json

package: sbom
>mkdir -p dist
>zip -r dist/dependabot-automerge-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md src tests Makefile sbom.json

canary:
>echo "Launching canary deployment"
