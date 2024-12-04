# test_client.py
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient  # Assuming GithubOrgClient is in the client module

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @patch("client.GithubOrgClient.get_json")
    @patch("client.GithubOrgClient._public_repos_url", return_value="https://api.github.com/orgs/google/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that the public_repos method returns the expected list of repos."""

        # Define the mock payload to be returned by get_json
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        # Create an instance of GithubOrgClient with a mock organization name
        client = GithubOrgClient("google")

        # Call the public_repos method
        repos = client.public_repos()

        # Test that the public_repos method returns the expected list of repo names
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        # Ensure that the _public_repos_url property was accessed once
        mock_public_repos_url.assert_called_once()

        # Ensure that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

if __name__ == "__main__":
    unittest.main()
