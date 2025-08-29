class RetryableError(Exception):
    """Exception indicating the operation can be retried."""


class TerminalError(Exception):
    """Exception indicating the operation should not be retried."""
