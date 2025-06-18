import unittest
from models import Repository

class TestRepository(unittest.TestCase):
    def test_repository_creation(self):
        repo = Repository("repo1", "https://github.com/user/repo1")
        self.assertEqual(repo.name, "repo1")
        self.assertEqual(repo.url, "https://github.com/user/repo1")

if __name__ == "__main__":
    unittest.main()
