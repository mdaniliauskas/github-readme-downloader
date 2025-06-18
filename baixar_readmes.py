import os
import requests

GITHUB_USER = "mdaniliauskas"
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
OUTPUT_DIR = "readmes"

os.makedirs(OUTPUT_DIR, exist_ok=True)

response = requests.get(API_URL, headers=HEADERS)
repos = response.json()

for repo in repos:
    repo_name = repo["name"]
    readme_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/main/README.md"
    r = requests.get(readme_url)
    if r.status_code == 404:
        readme_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/master/README.md"
        r = requests.get(readme_url)
    if r.status_code == 200:
        with open(os.path.join(OUTPUT_DIR, f"{repo_name}_README.md"), "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"Baixado: {repo_name}")
    else:
        print(f"README não encontrado para: {repo_name}")
