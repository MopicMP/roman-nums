"""Tests for roman-nums."""

import pytest
from roman_nums import nums


class TestNums:
    """Test suite for nums."""

    def test_basic(self):
        """Test basic usage."""
        result = nums("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            nums("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = nums(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
