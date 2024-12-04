#!/usr/bin/env python3
"""
Unit tests for the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test GithubOrgClient._public_repos_url.
        Mock the org property to return a known payload.
        """
        # Mock the org property to return a specific dictionary
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test_org")

        # Call the _public_repos_url property
        result = client._public_repos_url

        # Assertions
        self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
