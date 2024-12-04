#!/usr/bin/env python3
"""
Unit tests for the client module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test GithubOrgClient.org method.
        Mock the get_json function to avoid actual HTTP calls.
        """
        # Set up the mock to return the expected data
        mock_get_json.return_value = expected

        # Create an instance of GithubOrgClient and call the org method
        client = GithubOrgClient(org_name)
        result = client.org

        # Assertions
        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == "__main__":
    unittest.main()
