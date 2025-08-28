"""Tests for ethical check functionality."""

import os
from unittest.mock import patch

import pytest

from src import ethicalcheck


class TestEthicalCheck:
    """Test ethical check module functionality."""
    
    def test_validate_url_valid_https(self):
        """Test URL validation with valid HTTPS URL."""
        assert ethicalcheck._validate_url("https://api.example.com/openapi.json")
    
    def test_validate_url_valid_http(self):
        """Test URL validation with valid HTTP URL."""
        assert ethicalcheck._validate_url("http://localhost:8080/swagger.json")
    
    def test_validate_url_invalid_scheme(self):
        """Test URL validation with invalid scheme."""
        assert not ethicalcheck._validate_url("ftp://example.com/api.json")
    
    def test_validate_url_malformed(self):
        """Test URL validation with malformed URL."""
        assert not ethicalcheck._validate_url("not-a-url")
    
    def test_validate_url_empty(self):
        """Test URL validation with empty string."""
        assert not ethicalcheck._validate_url("")
    
    def test_validate_email_valid(self):
        """Test email validation with valid email."""
        assert ethicalcheck._validate_email("test@example.com")
        assert ethicalcheck._validate_email("user.name+tag@domain.co.uk")
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid email."""
        assert not ethicalcheck._validate_email("invalid-email")
        assert not ethicalcheck._validate_email("@example.com")
        assert not ethicalcheck._validate_email("test@")
        assert not ethicalcheck._validate_email("")
    
    @patch.dict(os.environ, {}, clear=True)
    def test_validate_configuration_missing_vars(self):
        """Test configuration validation with missing environment variables."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "skipped"
        assert result["reason"] == "missing_configuration"
    
    @patch.dict(os.environ, {"ETHICALCHECK_OAS_URL": "https://api.example.com/openapi.json"}, clear=True)
    def test_validate_configuration_missing_email(self):
        """Test configuration validation with missing email."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "skipped"
        assert result["reason"] == "missing_configuration"
    
    @patch.dict(os.environ, {"ETHICALCHECK_EMAIL": "test@example.com"}, clear=True)
    def test_validate_configuration_missing_url(self):
        """Test configuration validation with missing URL."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "skipped"
        assert result["reason"] == "missing_configuration"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "invalid-url",
        "ETHICALCHECK_EMAIL": "test@example.com"
    }, clear=True)
    def test_validate_configuration_invalid_url(self):
        """Test configuration validation with invalid URL."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "error"
        assert result["reason"] == "invalid_url"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "https://api.example.com/openapi.json",
        "ETHICALCHECK_EMAIL": "invalid-email"
    }, clear=True)
    def test_validate_configuration_invalid_email(self):
        """Test configuration validation with invalid email."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "error"
        assert result["reason"] == "invalid_email"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "https://api.example.com/openapi.json",
        "ETHICALCHECK_EMAIL": "test@example.com"
    }, clear=True)
    def test_validate_configuration_valid(self):
        """Test configuration validation with valid parameters."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "configured"
        assert result["url"] == "https://api.example.com/openapi.json"
        assert result["email"] == "test@example.com"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "  https://api.example.com/openapi.json  ",
        "ETHICALCHECK_EMAIL": "  test@example.com  "
    }, clear=True)
    def test_validate_configuration_strips_whitespace(self):
        """Test configuration validation strips whitespace."""
        result = ethicalcheck.validate_configuration()
        assert result["status"] == "configured"
        assert result["url"] == "https://api.example.com/openapi.json"
        assert result["email"] == "test@example.com"
    
    @patch.dict(os.environ, {}, clear=True)
    def test_main_missing_configuration(self):
        """Test main function with missing configuration."""
        result = ethicalcheck.main()
        assert result["status"] == "skipped"
        assert result["reason"] == "missing_configuration"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "invalid-url",
        "ETHICALCHECK_EMAIL": "test@example.com"
    }, clear=True)
    def test_main_invalid_configuration(self):
        """Test main function with invalid configuration."""
        result = ethicalcheck.main()
        assert result["status"] == "error"
        assert result["reason"] == "invalid_url"
    
    @patch.dict(os.environ, {
        "ETHICALCHECK_OAS_URL": "https://api.example.com/openapi.json",
        "ETHICALCHECK_EMAIL": "test@example.com"
    }, clear=True)
    def test_main_valid_configuration(self):
        """Test main function with valid configuration."""
        result = ethicalcheck.main()
        assert result["status"] == "ok"
        assert "message" in result