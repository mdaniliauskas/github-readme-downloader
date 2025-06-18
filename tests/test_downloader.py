import unittest
import os
from downloader import ReadmeDownloader
from models import Repository

class TestReadmeDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = ReadmeDownloader("mdaniliauskas", "test_readmes", "test_log.txt", delay=0)
        os.makedirs("test_readmes", exist_ok=True)

    def tearDown(self):
        if os.path.exists("test_log.txt"):
            os.remove("test_log.txt")
        for f in os.listdir("test_readmes"):
            os.remove(os.path.join("test_readmes", f))
        os.rmdir("test_readmes")

    def test_baixar_readmes_empty(self):
        self.downloader.baixar_readmes([])
        self.assertTrue(os.path.exists("test_log.txt"))
        with open("test_log.txt", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Total de repositórios: 0", content)

if __name__ == "__main__":
    unittest.main()
