from . import errors, fuzz, ingest, report, rollback, scan
from .config import Config


def run(cfg: Config | None = None) -> str:
    """Execute the workflow and return path to the report."""
    cfg = cfg or Config()
    try:
        data = ingest.main(cfg)
        fuzzed = fuzz.main(data, cfg)
        findings = scan.main(fuzzed, cfg)
        return report.main(findings, cfg)
    except (errors.RetryableError, errors.TerminalError) as exc:
        rollback.perform(str(exc))
        raise


if __name__ == "__main__":
    run()
