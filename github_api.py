import requests
import logging
from models import Repository

class GitHubAPI:
    """Responsável por interagir com a API do GitHub."""
    def __init__(self, user):
        self.user = user
        self.api_url = f"https://api.github.com/users/{user}/repos"
        self.headers = {"Accept": "application/vnd.github.v3+json"}

    def get_repositories(self):
        repos = []
        page = 1
        while True:
            paged_url = f"{self.api_url}?per_page=100&page={page}"
            try:
                response = requests.get(paged_url, headers=self.headers, timeout=10)
                if response.status_code == 404:
                    print(f"\n❗ Usuário '{self.user}' não encontrado no GitHub. Verifique o nome e tente novamente.")
                    return []
                data = response.json()
                if not data or response.status_code != 200:
                    break
                for repo in data:
                    repos.append(Repository(repo["name"], repo["html_url"]))
                if len(data) < 100:
                    break
                page += 1
            except Exception as e:
                logging.error(f"Erro ao buscar repositórios: {e}")
                break
        return repos
