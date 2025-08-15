.PHONY: venv bench api relay clean

PY := .venv/bin/python
PIP := .venv/bin/pip

venv:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

api:
	$(PY) 01_code/agent/main.py --api

relay:
	$(PY) 01_code/relay/main.py

bench:
	$(PY) 04_benchmarks/suites/synthetic/scripts/sim_duality.py --sweep \
		--out-details 04_benchmarks/results/S49_extended_details.csv \
		--out-summary 04_benchmarks/results/S49_extended_summary.csv

clean:
	rm -rf .venv 04_benchmarks/results/*.csv
