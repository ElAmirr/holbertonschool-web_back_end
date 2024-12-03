#!/usr/bin/env python3
"""
Unit tests for utils.get_json.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns the expected payload."""
        # Set up the mock to return a Mock object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)  # Ensure requests.get is called with the correct URL
        self.assertEqual(result, test_payload)  # Ensure the returned payload matches the expected payload


if __name__ == "__main__":
    unittest.main()
