.PHONY: test build sbom sign package

IMAGE?=fuzzing_vuln_scan:latest

test:
	pytest -q

build:
	docker build -t $(IMAGE) .

sbom:
	syft . -o json > sbom.json

sign:
	cosign sign $(IMAGE)

package:
	mkdir -p dist
	zip -r dist/fuzzing_vuln_scan-bundle.zip workflow_manifest.json integration_contract.md observability.yaml governance.yaml cost_model.md security.md src tests Makefile
