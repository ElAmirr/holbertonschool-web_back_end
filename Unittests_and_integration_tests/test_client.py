import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient  # Ensure to import the actual class from the client module
import fixtures

@parameterized_class([
    {"org_payload": fixtures.org_payload, "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos, "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get')

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Mock the return values based on URL
        cls.mock_get.side_effect = lambda url: cls._mock_get_response(url)

    @classmethod
    def _mock_get_response(cls, url):
        if url == "https://api.github.com/orgs/test_org":
            return cls.MockResponse(cls.org_payload)
        elif url == "https://api.github.com/orgs/test_org/repos":
            return cls.MockResponse(cls.repos_payload)
        return cls.MockResponse(None, status=404)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    class MockResponse:
        def __init__(self, json_data, status=200):
            self.json_data = json_data
            self.status_code = status

        def json(self):
            return self.json_data

    def test_public_repos(self):
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license_key="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

if __name__ == '__main__':
    unittest.main()
