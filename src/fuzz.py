from typing import Optional

from .config import Config
from .errors import RetryableError
from .logging_utils import log


def main(data: bytes, cfg: Optional[Config] = None) -> bytes:
    cfg = cfg or Config()
    log("fuzz.start")
    if cfg.fail_step:
        raise RetryableError("Injected failure for testing")
    log("fuzz.complete", cases=1)
    return data
