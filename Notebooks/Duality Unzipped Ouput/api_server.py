from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class PolicyUpdate(BaseModel):
    lte_budget_mb: Optional[int] = None
    parity_max_pct: Optional[float] = None
    jitter_hold_ms: Optional[int] = None

def build_app(state):
    app = FastAPI(title="DUALITY Agent API", version="0.1.0")

    @app.get("/health")
    def health():
        return {"ok": True, "state": "running"}

    @app.get("/policy")
    def get_policy():
        return {
            "lte_budget_mb": state["policy"].lte_budget_mb_day,
            "parity_max_pct": state["policy"].parity_max_pct,
            "jitter_hold_ms": state["policy"].jitter_hold_ms_cap,
        }

    @app.post("/policy", status_code=204)
    def set_policy(p: PolicyUpdate):
        if p.lte_budget_mb is not None:
            state["policy"].lte_budget_mb_day = int(p.lte_budget_mb)
        if p.parity_max_pct is not None:
            state["policy"].parity_max_pct = float(p.parity_max_pct)
        if p.jitter_hold_ms is not None:
            state["policy"].jitter_hold_ms_cap = int(p.jitter_hold_ms)
        return None

    @app.get("/stats")
    def stats():
        return state["dataplane"].stats()

    return app
