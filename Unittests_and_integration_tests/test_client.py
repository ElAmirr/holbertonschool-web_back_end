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
