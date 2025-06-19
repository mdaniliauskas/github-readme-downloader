import unittest
from unittest.mock import patch, MagicMock
from github_api import GitHubAPI
from downloader import ReadmeDownloader
from models import Repository
import os

class TestErrorScenarios(unittest.TestCase):
    @patch('requests.get')
    def test_github_api_network_error(self, mock_get):
        mock_get.side_effect = Exception("Network error")
        api = GitHubAPI("mdaniliauskas")
        repos = api.get_repositories()
        self.assertEqual(repos, [])

    @patch('requests.get')
    def test_downloader_network_error(self, mock_get):
        mock_get.side_effect = Exception("Network error")
        downloader = ReadmeDownloader("mdaniliauskas", "test_readmes", "test_log.txt", delay=0)
        os.makedirs("test_readmes", exist_ok=True)
        repo = Repository("repo1", "https://github.com/user/repo1")
        downloader.baixar_readmes([repo])
        with open("test_log.txt", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Total de repositórios: 1", content)
        for f in os.listdir("test_readmes"):
            os.remove(os.path.join("test_readmes", f))
        os.rmdir("test_readmes")
        os.remove("test_log.txt")

    def test_downloader_permission_error(self):
        # Simula permissão negada criando um diretório somente leitura
        os.makedirs("readonly_dir", exist_ok=True)
        os.chmod("readonly_dir", 0o444)
        downloader = ReadmeDownloader("mdaniliauskas", "readonly_dir", "test_log.txt", delay=0)
        repo = Repository("repo1", "https://github.com/user/repo1")
        try:
            downloader.baixar_readmes([repo])
        except Exception as e:
            self.assertIsInstance(e, PermissionError)
        finally:
            os.chmod("readonly_dir", 0o755)
            os.rmdir("readonly_dir")
            if os.path.exists("test_log.txt"):
                os.remove("test_log.txt")

if __name__ == "__main__":
    unittest.main()
