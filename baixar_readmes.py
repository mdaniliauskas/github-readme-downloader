import os
import requests

GITHUB_USER = input("Digite o nome de usuário do GitHub para baixar os READMEs: ")
API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"
HEADERS = {"Accept": "application/vnd.github.v3+json"}
OUTPUT_DIR = "readmes"
LOG_FILE = "log_readmes.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paginação para pegar todos os repositórios
dados_repos = []
page = 1
while True:
    paged_url = f"{API_URL}?per_page=100&page={page}"
    response = requests.get(paged_url, headers=HEADERS)
    data = response.json()
    if not data or response.status_code != 200:
        break
    dados_repos.extend(data)
    if len(data) < 100:
        break
    page += 1

total = len(dados_repos)
baixados = []
nao_baixados = []

for repo in dados_repos:
    repo_name = repo["name"]
    repo_url = repo["html_url"]
    readme_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/main/README.md"
    r = requests.get(readme_url)
    if r.status_code == 404:
        readme_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{repo_name}/master/README.md"
        r = requests.get(readme_url)
    if r.status_code == 200:
        with open(os.path.join(OUTPUT_DIR, f"{repo_name}_README.md"), "w", encoding="utf-8") as f:
            f.write(r.text)
        msg = f"✅ Baixado: {repo_name} | {repo_url}"
        baixados.append(msg)
        print(msg)
    else:
        msg = f"❌ Sem README: {repo_name} | {repo_url}"
        nao_baixados.append(msg)
        print(msg)

# Escreve o log organizado
with open(LOG_FILE, "w", encoding="utf-8") as logf:
    logf.write("# Repositórios com README baixado\n")
    for line in baixados:
        logf.write(line + "\n")
    logf.write(f"\nTotal com README: {len(baixados)}\n\n")
    logf.write("# Repositórios sem README\n")
    for line in nao_baixados:
        logf.write(line + "\n")
    logf.write(f"\nTotal sem README: {len(nao_baixados)}\n\n")
    logf.write(f"Total de repositórios: {total}\n")

# Print final
print(f"\nResumo:")
print(f"Total de repositórios: {total}")
print(f"Com README: {len(baixados)}")
print(f"Sem README: {len(nao_baixados)}")
print("\n📄 Veja o log completo e organizado em: log_readmes.txt (com separação dos repositórios com e sem README)")
