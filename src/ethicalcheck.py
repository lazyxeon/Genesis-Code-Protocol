from __future__ import annotations

import os
import re
from urllib.parse import urlparse

from .utils import get_logger

logger = get_logger(__name__)


def _validate_url(url: str) -> bool:
    """Validate URL format for OpenAPI specification."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and result.scheme in ('http', 'https')
    except Exception:
        return False


def _validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_configuration() -> dict[str, str]:
    """Validate EthicalCheck configuration parameters."""
    oas_url = os.getenv("ETHICALCHECK_OAS_URL", "").strip()
    email = os.getenv("ETHICALCHECK_EMAIL", "").strip()

    if not oas_url or not email:
        logger.info("EthicalCheck configuration incomplete - skipping scan")
        return {"status": "skipped", "reason": "missing_configuration"}

    if not _validate_url(oas_url):
        logger.error(f"Invalid OpenAPI specification URL: {oas_url}")
        return {"status": "error", "reason": "invalid_url"}

    if not _validate_email(email):
        logger.error(f"Invalid email address: {email}")
        return {"status": "error", "reason": "invalid_email"}

    logger.info(f"EthicalCheck configuration validated - URL: {oas_url}, Email: {email}")
    return {"status": "configured", "url": oas_url, "email": email}


def main() -> dict[str, str]:
    """Execute EthicalCheck scan with proper validation."""
    config_result = validate_configuration()

    if config_result["status"] != "configured":
        return config_result

    logger.info("EthicalCheck scan initiated")

    # The actual scan is performed by the GitHub Action
    # This function validates configuration and logs the process
    return {"status": "ok", "message": "EthicalCheck scan configuration validated"}
