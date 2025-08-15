import yaml
from dataclasses import dataclass

@dataclass
class Policy:
    lte_budget_mb_day: int = 200
    parity_max_pct: float = 0.10
    jitter_hold_ms_cap: int = 22

def load_policy(path: str) -> Policy:
    with open(path, "r") as f:
        data = yaml.safe_load(f) or {}
    return Policy(
        lte_budget_mb_day=int(data.get("lte_budget_mb", 200)),
        parity_max_pct=float(data.get("parity_max_pct", 0.10)),
        jitter_hold_ms_cap=int(data.get("jitter_hold_ms", 22)),
    )
