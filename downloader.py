import os
import requests
import time
import logging
from tqdm import tqdm
from models import Repository
import csv

class ReadmeDownloader:
    """
    Responsável por baixar e salvar os READMEs dos repositórios.

    Args:
        user (str): Nome de usuário do GitHub.
        output_dir (str): Diretório de saída dos arquivos README.
        log_file (str): Caminho do arquivo de log.
        delay (float): Delay entre requisições (segundos).
    """
    def __init__(self, user, output_dir, log_file, delay=0.5):
        """
        Inicializa o downloader.

        Args:
            user (str): Nome de usuário do GitHub.
            output_dir (str): Diretório de saída dos arquivos README.
            log_file (str): Caminho do arquivo de log.
            delay (float, opcional): Delay entre requisições (segundos). Default: 0.5
        """
        self.user = user
        self.output_dir = output_dir
        self.log_file = log_file
        self.delay = delay
        self.readme_variants = ["README.md", "Readme.md", "readme.md", "ReadMe.md", "readME.md"]
        os.makedirs(self.output_dir, exist_ok=True)

    def baixar_readmes(self, repos):
        """
        Baixa os READMEs dos repositórios fornecidos.

        Args:
            repos (list[Repository]): Lista de repositórios para baixar os READMEs.
        """
        baixados = []
        nao_baixados = []
        baixados_csv = []
        nao_baixados_csv = []
        for repo in tqdm(repos, desc="Processando repositórios"):
            readme_found = False
            for variant in self.readme_variants:
                for branch in ["main", "master"]:
                    readme_url = f"https://raw.githubusercontent.com/{self.user}/{repo.name}/{branch}/{variant}"
                    try:
                        r = requests.get(readme_url, timeout=10)
                        if r.status_code == 200:
                            with open(os.path.join(self.output_dir, f"{repo.name}_README.md"), "w", encoding="utf-8") as f:
                                f.write(r.text)
                            msg = f"✅ Baixado: {repo.name} | {repo.url}"
                            baixados.append(msg)
                            baixados_csv.append([repo.name, repo.url, "Baixado"])
                            print(msg)
                            readme_found = True
                            break
                    except Exception as e:
                        logging.warning(f"Erro ao baixar README de {repo.name}: {e}")
                if readme_found:
                    break
            if not readme_found:
                msg = f"❌ Sem README: {repo.name} | {repo.url}"
                nao_baixados.append(msg)
                nao_baixados_csv.append([repo.name, repo.url, "Sem README"])
                print(msg)
            time.sleep(self.delay)
        self._gerar_log(baixados, nao_baixados, len(repos))
        self._gerar_csv(baixados_csv, nao_baixados_csv)

    def _gerar_log(self, baixados, nao_baixados, total):
        """
        Gera o log de execução do processo.

        Args:
            baixados (list): Lista de repositórios baixados.
            nao_baixados (list): Lista de repositórios sem README.
            total (int): Total de repositórios processados.
        """
        with open(self.log_file, "w", encoding="utf-8") as logf:
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

    def _gerar_csv(self, baixados_csv, nao_baixados_csv):
        """
        Gera o relatório CSV com o status dos repositórios.

        Args:
            baixados_csv (list): Linhas de repositórios baixados.
            nao_baixados_csv (list): Linhas de repositórios sem README.
        """
        with open("relatorio_readmes.csv", "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Repositório", "URL", "Status"])
            for row in baixados_csv:
                writer.writerow(row)
            for row in nao_baixados_csv:
                writer.writerow(row)
        print("\n📊 Relatório CSV gerado: relatorio_readmes.csv")
