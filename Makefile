.PHONY: install lint test sbom build canary

install:
	pip install -r requirements.txt

lint:
	flake8 src tests

test:
	pytest -q

sbom:
	syft . -o json > sbom.json

build:
	docker build -t matrix-ci .

canary:
	echo "Launching canary deployment"
