import os
import requests

# Substitua pelo seu usuário do GitHub
GITHUB_USER = input("Digite o nome de usuário do GitHub para baixar os READMEs: ")
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
OUTPUT_DIR = "readmes"
LOG_FILE = "log_readmes.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paginação para pegar todos os repositórios
repos = []
page = 1
while True:
    paged_url = f"{API_URL}?per_page=100&page={page}"
    response = requests.get(paged_url, headers=HEADERS)
    data = response.json()
    if not data or response.status_code != 200:
        break
    repos.extend(data)
    if len(data) < 100:
        break
    page += 1

log_lines = []
baixados = 0
nao_baixados = 0

total = len(repos)
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
        msg = f"Baixado: {repo_name}"
        log_lines.append(msg)
        print(msg)
        baixados += 1
    else:
        msg = f"README não encontrado para: {repo_name}"
        log_lines.append(msg)
        print(msg)
        nao_baixados += 1

# Escreve o log sobrescrevendo o anterior
with open(LOG_FILE, "w", encoding="utf-8") as logf:
    for line in log_lines:
        logf.write(line + "\n")
    logf.write(f"\nTotal de repositórios: {total}\n")
    logf.write(f"Baixados: {baixados}\n")
    logf.write(f"Não baixados: {nao_baixados}\n")

# Print final
print(f"Total de repositórios: {total}")
print(f"Baixados: {baixados}")
print(f"Não baixados: {nao_baixados}")
