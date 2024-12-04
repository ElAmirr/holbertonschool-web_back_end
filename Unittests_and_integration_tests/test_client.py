#!/usr/bin/env python3
"""
Unit tests for the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
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
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        Mock get_json and _public_repos_url.
        """
        mock_repos = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_repos

        with patch.object(GithubOrgClient, "_public_repos_url", new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"
            client = GithubOrgClient("test-org")
            repos = client.public_repos
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test GithubOrgClient.has_license method.
        Check if the repo has the given license key.
        """
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
