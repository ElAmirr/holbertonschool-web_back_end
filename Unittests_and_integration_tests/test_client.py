# test_client.py
import unittest
from unittest.mock import patch
from client import GithubOrgClient  # Assuming GithubOrgClient is in the client module

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @patch("client.GithubOrgClient.org")
    def test_public_repos_url(self, mock_org):
        """Test that the _public_repos_url method returns the correct value based on the mocked org."""
        
        # Mock the org property to return a specific payload
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Create a GithubOrgClient instance
        client = GithubOrgClient("google")

        # Call _public_repos_url to check the result
        repos_url = client._public_repos_url
        
        # Test that the _public_repos_url method returns the expected URL
        self.assertEqual(repos_url, "https://api.github.com/orgs/google/repos")

        # Ensure that the org method (property) was accessed
        mock_org.assert_called_once()

if __name__ == "__main__":
    unittest.main()
