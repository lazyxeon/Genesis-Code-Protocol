<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
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
=======
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
>>>>>> main
