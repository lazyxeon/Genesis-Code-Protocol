from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Callable, List

from pydantic import BaseModel, Field

try:  # pragma: no cover - OTEL optional
    from opentelemetry import trace

    tracer = trace.get_tracer(__name__)
except Exception:  # pragma: no cover

    class DummyTracer:
        def start_as_current_span(self, name: str):
            from contextlib import contextmanager

            @contextmanager
            def span():
                yield

            return span()

    tracer = DummyTracer()

logger = logging.getLogger("matrix_ci")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class EnvConfig(BaseModel):
    """Configuration for matrix CI steps."""

    python_versions: List[str] = Field(..., min_items=1)


def _log(step: str, message: str) -> None:
    logger.info(json.dumps({"step": step, "message": message}))


def setup_env(config: EnvConfig) -> bool:
    with tracer.start_as_current_span("setup"):
        _log("setup", f"environment ready for {config.python_versions}")
        return True


def run_lint(config: EnvConfig) -> bool:
    with tracer.start_as_current_span("lint"):
        _log("lint", "lint passed")
        return True


def run_tests(config: EnvConfig) -> bool:
    with tracer.start_as_current_span("test"):
        _log("test", f"tests passed on {config.python_versions}")
        return True


def run_all(config: EnvConfig) -> bool:
    return setup_env(config) and run_lint(config) and run_tests(config)


@dataclass
class RollbackState:
    executed_steps: List[str]


def run_with_failure(
    step: Callable[[EnvConfig], bool], config: EnvConfig
) -> RollbackState:
    state = RollbackState(executed_steps=[])
    try:
        setup_env(config)
        state.executed_steps.append("setup")
        step(config)
        state.executed_steps.append("step")
    except Exception:
        rollback(state)
    return state


def rollback(state: RollbackState) -> None:
    _log("rollback", f"reverting steps: {state.executed_steps}")
