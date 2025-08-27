<<<<<< codex/develop-and-implement-matrix-ci
.PHONY: install lint test sbom build canary

install:
	pip install -r requirements.txt

lint:
	flake8 src tests
=======
<<<<<< codex/analyze-failing-github-workflows
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
=======
<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
.PHONY: test build sbom sign package

IMAGE?=fuzzing_vuln_scan:latest
>>>>>> main

test:
	pytest -q

<<<<<< codex/develop-and-implement-matrix-ci
sbom:
	syft . -o json > sbom.json

build:
	docker build -t matrix-ci .

canary:
	echo "Launching canary deployment"
=======
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
>>>>>> main
>>>>>> main
