#!/usr/bin/env python3
"""
Unit tests for the client module with parameterization and patching.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @patch("client.GithubOrgClient.get_json")
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        - Mock get_json to ensure no HTTP calls are made.
        - Parametrize test with two organization names: google, abc.
        """
        # Set up the mock for get_json to return a known payload
        mock_get_json.return_value = {"org": org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org property
        result = client.org

        # Assertions
        self.assertEqual(result, {"org": org_name})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        

if __name__ == "__main__":
    unittest.main()
