import os
import requests
import time
import logging
from tqdm import tqdm
import argparse

def get_repos(user):
    """Busca todos os repositórios públicos de um usuário do GitHub."""
    API_URL = f"https://api.github.com/users/{user}/repos"
    HEADERS = {"Accept": "application/vnd.github.v3+json"}
    repos = []
    page = 1
    while True:
        paged_url = f"{API_URL}?per_page=100&page={page}"
        try:
            response = requests.get(paged_url, headers=HEADERS, timeout=10)
            if response.status_code == 404:
                print(f"\n❗ Usuário '{user}' não encontrado no GitHub. Verifique o nome e tente novamente.")
                return []
            data = response.json()
            if not data or response.status_code != 200:
                break
            repos.extend(data)
            if len(data) < 100:
                break
            page += 1
        except Exception as e:
            logging.error(f"Erro ao buscar repositórios: {e}")
            break
    return repos

def baixar_readmes(user, output_dir, log_file, delay=0.5):
    os.makedirs(output_dir, exist_ok=True)
    repos = get_repos(user)
    if not repos:
        print("Processo abortado.")
        return
    total = len(repos)
    baixados = []
    nao_baixados = []
    readme_variants = ["README.md", "Readme.md", "readme.md", "ReadMe.md", "readME.md"]
    for repo in tqdm(repos, desc="Processando repositórios"):
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        readme_found = False
        for variant in readme_variants:
            for branch in ["main", "master"]:
                readme_url = f"https://raw.githubusercontent.com/{user}/{repo_name}/{branch}/{variant}"
                try:
                    r = requests.get(readme_url, timeout=10)
                    if r.status_code == 200:
                        with open(os.path.join(output_dir, f"{repo_name}_README.md"), "w", encoding="utf-8") as f:
                            f.write(r.text)
                        msg = f"✅ Baixado: {repo_name} | {repo_url}"
                        baixados.append(msg)
                        print(msg)
                        readme_found = True
                        break
                except Exception as e:
                    logging.warning(f"Erro ao baixar README de {repo_name}: {e}")
            if readme_found:
                break
        if not readme_found:
            msg = f"❌ Sem README: {repo_name} | {repo_url}"
            nao_baixados.append(msg)
            print(msg)
        time.sleep(delay)
    # Log estruturado
    with open(log_file, "w", encoding="utf-8") as logf:
        logf.write("# Repositórios com README baixado\n")
        for line in baixados:
            logf.write(line + "\n")
        logf.write(f"\nTotal com README: {len(baixados)}\n\n")
        logf.write("# Repositórios sem README\n")
        for line in nao_baixados:
            logf.write(line + "\n")
        logf.write(f"\nTotal sem README: {len(nao_baixados)}\n\n")
        logf.write(f"Total de repositórios: {total}\n")
    print(f"\nResumo:")
    print(f"Total de repositórios: {total}")
    print(f"Com README: {len(baixados)}")
    print(f"Sem README: {len(nao_baixados)}")
    print("\n📄 Veja o log completo e organizado em: log_readmes.txt (com separação dos repositórios com e sem README)")

def main():
    parser = argparse.ArgumentParser(description="Baixa os READMEs de todos os repositórios públicos de um usuário do GitHub.")
    parser.add_argument("-u", "--user", type=str, help="Nome de usuário do GitHub", required=False)
    parser.add_argument("-o", "--output", type=str, default="readmes", help="Diretório de saída")
    parser.add_argument("-l", "--log", type=str, default="log_readmes.txt", help="Arquivo de log")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Delay entre requisições (segundos)")
    args = parser.parse_args()
    user = args.user or input("Digite o nome de usuário do GitHub para baixar os READMEs: ")
    baixar_readmes(user, args.output, args.log, args.delay)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main()
