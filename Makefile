.RECIPEPREFIX := >
.PHONY: install test build sbom sign package

install:
>pip install -r requirements.txt

test:
>pytest -q

build:
>docker build -t matrix-ci-repair .

sbom:
>syft . -o json > sbom.json

sign:
>cosign sign-blob --key $$COSIGN_KEY sbom.json

package: build sbom
>mkdir -p dist
>zip -r dist/matrix-ci-repair-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md tests src Makefile sbom.json
