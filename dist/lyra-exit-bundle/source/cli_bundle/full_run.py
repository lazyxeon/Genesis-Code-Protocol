"""Utilities for executing the full GRCP run."""


def execute_full_run(prompt: str, version: str, risk_tier: str) -> None:
    """Simulate running all phases for ``prompt`` and ``version``."""
    print(f"Executing full GRCP run for v{version}, tier {risk_tier}...")
    # Simulate phases; in real, call phase scripts or LLM
    phases = ["-1", "0", "1", "2", "3", "4", "5", "6", "7"]
    for phase in phases:
        print(f"Running Phase {phase} with prompt: {prompt}")
        # Placeholder: Call phase script or LLM API
    print("Full run complete. Outputs in logs.")
