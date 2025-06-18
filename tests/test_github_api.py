import unittest
from github_api import GitHubAPI

class TestGitHubAPI(unittest.TestCase):
    def test_get_repositories_invalid_user(self):
        api = GitHubAPI("usuario_inexistente_1234567890")
        repos = api.get_repositories()
        self.assertEqual(repos, [])

if __name__ == "__main__":
    unittest.main()
