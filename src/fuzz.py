from .config import Config
from .logging_utils import log
from .errors import RetryableError


def main(data: bytes, cfg: Config | None = None) -> bytes:
    cfg = cfg or Config()
    log("fuzz.start")
    if cfg.fail_step:
        raise RetryableError("Injected failure for testing")
    log("fuzz.complete", cases=1)
    return data
