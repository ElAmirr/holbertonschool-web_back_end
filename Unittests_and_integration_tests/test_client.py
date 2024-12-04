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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        Mock get_json and _public_repos_url to return predefined values.
        """
        # Mock data for the test
        org_name = "google"
        repos_payload = [{"name": "repo1"}, {"name": "repo2"}]
        expected_url = f"https://api.github.com/orgs/{org_name}/repos"

        # Use patch to mock the _public_repos_url property
        with patch.object(GithubOrgClient, "_public_repos_url", return_value=expected_url):
            # Mock the response for get_json
            mock_get_json.return_value = repos_payload

            # Create an instance of GithubOrgClient and call the public_repos method
            client = GithubOrgClient(org_name)
            result = client.public_repos()

            # Assertions
            self.assertEqual(result, repos_payload)
            mock_get_json.assert_called_once_with(expected_url)

if __name__ == "__main__":
    unittest.main()
