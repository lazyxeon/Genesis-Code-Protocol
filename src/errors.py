"""Error taxonomy for workflow steps."""

class RetryableError(Exception):
    """An error indicating the step may be retried."""

class TerminalError(Exception):
    """An error indicating the workflow should halt."""
