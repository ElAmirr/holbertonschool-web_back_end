#!/usr/bin/env python3
"""
Unit tests and integration tests for the client module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up class: mock requests.get."""
        cls.get_patcher = patch("requests.get")

        # Start patcher and set side_effect for different URLs
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mocked_requests_get

    @classmethod
    def tearDownClass(cls):
        """Tear down class: stop patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mocked requests.get to return appropriate payloads based on URL.
        """
        if url == "https://api.github.com/orgs/google":
            return MockResponse(org_payload, 200)
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(repos_payload, 200)
        return MockResponse(None, 404)

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("google")
        result = client.public_repos
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with a specific license."""
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)


class MockResponse:
    """Mock class for requests.Response."""

    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """Return the JSON data."""
        return self.json_data


if __name__ == "__main__":
    unittest.main()
