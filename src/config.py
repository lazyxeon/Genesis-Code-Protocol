import os
from dataclasses import dataclass, field


@dataclass
class Config:
    source_archive: str = field(
        default_factory=lambda: os.getenv("WF_SOURCE_ARCHIVE", "sample.tar.gz")
    )
    report_path: str = field(
        default_factory=lambda: os.getenv("WF_REPORT_PATH", "report.json")
    )
    fail_step: bool = field(
        default_factory=lambda: os.getenv("WF_FAIL_STEP", "false").lower() == "true"
    )
