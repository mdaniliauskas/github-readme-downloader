import argparse
import logging
from github_api import GitHubAPI
from downloader import ReadmeDownloader

def main():
    parser = argparse.ArgumentParser(description="Baixa os READMEs de todos os repositórios públicos de um usuário do GitHub.")
    parser.add_argument("-u", "--user", type=str, help="Nome de usuário do GitHub", required=False)
    parser.add_argument("-o", "--output", type=str, default="readmes", help="Diretório de saída")
    parser.add_argument("-l", "--log", type=str, default="log_readmes.txt", help="Arquivo de log")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Delay entre requisições (segundos)")
    args = parser.parse_args()
    user = args.user or input("Digite o nome de usuário do GitHub para baixar os READMEs: ")

    github = GitHubAPI(user)
    repos = github.get_repositories()
    if not repos:
        print("Processo abortado.")
        return
    downloader = ReadmeDownloader(user, args.output, args.log, args.delay)
    downloader.baixar_readmes(repos)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    main()
