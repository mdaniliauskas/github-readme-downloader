# Documentação da API (Funções e Classes)

Este documento descreve as principais classes e funções do projeto `github-readme-downloader`.

---

## models.py

### class Repository
Representa um repositório do GitHub.
- **name** (str): Nome do repositório.
- **url** (str): URL do repositório.

---

## github_api.py

### class GitHubAPI
Responsável por interagir com a API do GitHub.
- **__init__(user: str)**: Inicializa com o nome de usuário.
- **get_repositories() -> list[Repository]**: Retorna uma lista de objetos Repository dos repositórios públicos do usuário.

---

## downloader.py

### class ReadmeDownloader
Responsável por baixar e salvar os READMEs dos repositórios.
- **__init__(user: str, output_dir: str, log_file: str, delay: float = 0.5)**: Inicializa o downloader.
- **baixar_readmes(repos: list[Repository])**: Baixa os READMEs dos repositórios fornecidos.
- **_gerar_log(baixados, nao_baixados, total)**: Gera o log de execução.
- **_gerar_csv(baixados_csv, nao_baixados_csv)**: Gera o relatório CSV.

---

## baixar_readmes.py

### main()
Função principal, orquestra a execução do script via linha de comando.

---

> Para detalhes completos, consulte as docstrings no código-fonte.
