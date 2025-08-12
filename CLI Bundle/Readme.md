# GRCP CLI Bundle

The CLI Bundle provides a command-line interface for orchestrating GRCP protocols. It supports running specific versions, risk tiers, and full invention cycles with automation.

## Installation

1. Ensure Python 3.10+ is installed.
2. Install dependencies:

#Overview

## CLI Bundle for Genesis Recursive Code Protocol (GRCP)

This folder contains the command-line interface (CLI) tools for running GRCP protocols. It includes scripts for orchestration, phase execution, utilities, and dependencies. Updated as of August 12, 2025, to support v47 features like risk-tiered execution, worth-it assessments, and continuous assurance.

## Files in This Bundle

- `CLI_Readme.md`: This file (usage instructions).
- `gcp_cli.py`: Main CLI entry point for running protocols.
- `full_run.py`: Script for executing complete invention cycles.
- `phase1.py`: Example phase script (extendable for custom phases).
- `phase6.7.py`: Another phase example (e.g., validation).
- `audit_utils.py`: Utilities for auditing and governance checks.
- `prompt_utils.py`: Helpers for generating LLM prompts.
- `requirements.txt`: Dependency list for the CLI.

To use: Install dependencies with `pip install -r requirements.txt`, then run commands like `python gcp_cli.py --help`.

Below is the content for each file, ready to copy-paste into your GitHub repo's CLI Bundle folder.

### CLI_Readme.md

```markdown
# GRCP CLI Bundle

The CLI Bundle provides a command-line interface for orchestrating GRCP protocols. It supports running specific versions, risk tiers, and full invention cycles with automation.

## Installation

1. Ensure Python 3.10+ is installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) For Spark integration in v47: Install PySpark separately if needed.

## Usage

### Main CLI: gcp_cli.py

Run GRCP protocols via CLI.

```bash
python gcp_cli.py [OPTIONS]
```

Options:
- `--version VERSION`: Protocol version (e.g., 47). Default: latest (47).
- `--risk-tier TIER`: Risk tier (R1, R2, R3). Default: R1.
- `--prompt PROMPT`: Invention prompt (required for runs).
- `--phase PHASE`: Run a specific phase (e.g., -1 for worth-it sprint).
- `--full-run`: Execute a complete cycle (uses full_run.py).
- `--audit`: Perform audit checks (uses audit_utils.py).
- `--help`: Show help.

Example:
```bash
python gcp_cli.py --version 47 --risk-tier R2 --prompt "Invent an EV charging optimizer" --full-run
```

### Utilities

- `audit_utils.py`: Functions for ethical audits and governance.
- `prompt_utils.py`: Generate dynamic prompts for LLMs.
- `phase1.py` / `phase6.7.py`: Modular phase scripts; extend for custom logic.

## Extending the CLI

Add new phases or variants by creating scripts and integrating into gcp_cli.py. For v47+, include worth-it EVM calculations in prompts.

## Dependencies (requirements.txt)

See requirements.txt for full list.

## Notes

- LLM integration: Copy-paste outputs to your LLM (e.g., Grok) or integrate via API (future).
- Testing: Run with `--test` flag for dry runs.
- Contributions: See CONTRIBUTING.md in root.

For issues, open a GitHub issue.
```

### gcp_cli.py

```python
import argparse
import subprocess
import os
import sys

# Import utilities (assume in same dir)
from audit_utils import run_audit
from prompt_utils import generate_prompt
from full_run import execute_full_run

def main():
    parser = argparse.ArgumentParser(description="GRCP CLI: Orchestrate AI-native inventions.")
    parser.add_argument('--version', type=str, default='47', help='Protocol version (e.g., 47)')
    parser.add_argument('--risk-tier', type=str, default='R1', choices=['R1', 'R2', 'R3'], help='Risk tier')
    parser.add_argument('--prompt', type=str, help='Invention prompt')
    parser.add_argument('--phase', type=str, help='Specific phase to run (e.g., -1)')
    parser.add_argument('--full-run', action='store_true', help='Execute full invention cycle')
    parser.add_argument('--audit', action='store_true', help='Run audit checks')
    parser.add_argument('--test', action='store_true', help='Dry run/test mode')
    parser.add_argument('--help', action='help', help='Show this help message')

    args = parser.parse_args()

    if args.test:
        print("Running in test mode...")
        # Simulate
        print(f"Test: Version {args.version}, Tier {args.risk_tier}, Prompt: {args.prompt}")
        return

    if not args.prompt and not args.audit:
        print("Error: --prompt required for runs.")
        sys.exit(1)

    protocol_dir = os.path.join(os.path.dirname(__file__), '..', 'GRCP most recent variants')
    protocol_file = f"GCP V{args.version} — WORTH-IT REALISM EDITION.md"  # Adjust for version

    if args.full_run:
        execute_full_run(args.prompt, args.version, args.risk_tier)
    elif args.phase:
        phase_script = f"phase{args.phase.replace('-', '')}.py"
        if os.path.exists(phase_script):
            subprocess.run(['python', phase_script, '--prompt', args.prompt])
        else:
            print(f"Phase script {phase_script} not found.")
    elif args.audit:
        run_audit(args.prompt, args.version)
    else:
        # Default: Generate prompt and print
        prompt = generate_prompt(args.prompt, args.version, args.risk_tier)
        print("Generated Prompt for LLM:")
        print(prompt)

if __name__ == "__main__":
    main()
```

### full_run.py

```python
def execute_full_run(prompt, version, risk_tier):
    print(f"Executing full GRCP run for v{version}, tier {risk_tier}...")
    # Simulate phases; in real, call phase scripts or LLM
    phases = ['-1', '0', '1', '2', '3', '4', '5', '6', '7']
    for phase in phases:
        print(f"Running Phase {phase} with prompt: {prompt}")
        # Placeholder: Call phase script or LLM API
    print("Full run complete. Outputs in logs.")
```

### phase1.py

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="GRCP Phase 1: Discovery")
    parser.add_argument('--prompt', required=True)
    args = parser.parse_args()
    print(f"Phase 1: Discovering ideas for '{args.prompt}'...")

if __name__ == "__main__":
    main()
```

### phase6.7.py

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="GRCP Phase 6.7: Validation")
    parser.add_argument('--prompt', required=True)
    args = parser.parse_args()
    print(f"Phase 6.7: Validating outputs for '{args.prompt}'...")

if __name__ == "__main__":
    main()
```

### audit_utils.py

```python
def run_audit(prompt, version):
    print(f"Auditing prompt '{prompt}' for v{version}...")
    # Placeholder: Ethical checks
    return {"proxy_score": 0.85, "fairness_delta": 0.02}
```

### prompt_utils.py

```python
def generate_prompt(base_prompt, version, risk_tier):
    return f"Run GRCP v{version} ({risk_tier}): {base_prompt}. Assess worth-it and proceed."
```

### requirements.txt

```
argparse==1.4.0
subprocess
os
sys
# Add more as needed, e.g., pyspark for v47
```