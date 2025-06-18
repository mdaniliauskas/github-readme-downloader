[![Build Status](https://github.com/mdaniliauskas/github-readme-downloader/actions/workflows/python-app.yml/badge.svg)](https://github.com/mdaniliauskas/github-readme-downloader/actions)
[![Coverage Status](https://coveralls.io/repos/github/mdaniliauskas/github-readme-downloader/badge.svg?branch=main)](https://coveralls.io/github/mdaniliauskas/github-readme-downloader?branch=main)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# 📚 GitHub Readme Downloader

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-API-black?logo=github)
![tqdm](https://img.shields.io/badge/tqdm-barra%20de%20progresso-green)
![Testes](https://img.shields.io/badge/testes-automatizados-success)

## ✨ Motivação

Este projeto nasceu de uma necessidade prática e pode ser útil para qualquer pessoa que queira organizar e melhorar a documentação dos próprios repositórios. Compartilho aqui a solução para que outros possam se beneficiar, adaptar e contribuir conforme suas necessidades.

## 🚀 Sobre o Projeto

Este projeto foi evoluído para uma arquitetura orientada a objetos e modular, facilitando manutenção, testes e expansão. Ele automatiza:

1. Listar todos os repositórios públicos de um usuário do GitHub.
2. Baixar o arquivo README de cada repositório (tentando diferentes variações de nome e branch, como `README.md`, `Readme.md`, etc, nos ramos `main` e `master`).
3. Gerar um log detalhado e organizado, separando repositórios com e sem README, incluindo as URLs para fácil acesso.
4. Exibir uma barra de progresso visual durante o processo.
5. Permitir fácil adaptação para qualquer usuário do GitHub, inclusive via argumentos de linha de comando.
6. Tratar erros de rede, usuário inexistente e limitações de API.
7. Garantir confiabilidade por meio de testes automatizados.

### Estrutura do Projeto

```
github-readme-downloader/
├── baixar_readmes.py         # Ponto de entrada (main)
├── github_api.py             # Classe para comunicação com a API do GitHub
├── downloader.py             # Classe para download e salvamento dos READMEs
├── models.py                 # Classes de domínio (ex: Repository)
├── tests/                    # Testes automatizados
├── README.md
└── requirements.txt
```

> **Mentalidade:** Este projeto nasceu de uma necessidade prática e foi desenvolvido pensando em facilitar a vida de quem, assim como eu, deseja organizar e melhorar a documentação dos próprios repositórios. Compartilho a solução de forma aberta para que outros possam se beneficiar, adaptar e contribuir conforme suas necessidades.

## 🛠️ Como Usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/mdaniliauskas/github-readme-downloader.git
   cd github-readme-downloader
   ```
2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   # ou
   pip install requests tqdm pytest coverage
   ```
3. **Execute o script:**
   ```bash
   python baixar_readmes.py
   ```
   - O script pedirá o nome de usuário do GitHub (ou use `-u <usuario>` para rodar direto).
   - Os READMEs serão baixados na pasta `readmes` (ou outra, se desejar).
   - Um log detalhado será gerado ao final do processo, separando repositórios com e sem README.
   - Barra de progresso e mensagens visuais facilitam o acompanhamento.

### Exemplos de uso avançado

```bash
python baixar_readmes.py -u mdaniliauskas -o ./meus_readmes -l meu_log.txt -d 1
```

## 🐳 Uso com Docker

1. **Construa a imagem Docker:**
   ```sh
   docker build -t github-readme-downloader .
   ```
2. **Execute o container interativamente:**
   ```sh
   docker run -it --rm github-readme-downloader
   ```
   O script pedirá o nome de usuário do GitHub normalmente.

3. **Passe argumentos diretamente:**
   ```sh
   docker run --rm github-readme-downloader -u mdaniliauskas --loglevel DEBUG
   ```

4. **Mapeie volumes para acessar arquivos gerados:**
   ```sh
   docker run --rm -v %cd%/readmes:/app/readmes -v %cd%/relatorio_readmes.csv:/app/relatorio_readmes.csv github-readme-downloader -u mdaniliauskas
   ```
   > No Linux/Mac, use `$(pwd)` no lugar de `%cd%`.

## 🧪 Testes Automatizados

O projeto conta com testes unitários para os principais módulos, garantindo confiabilidade e facilitando futuras evoluções.

- Para rodar todos os testes:
  ```bash
  python -m unittest discover -v -s tests
  ```
- Para verificar a cobertura de testes:
  ```bash
  python -m coverage run -m unittest discover -s tests
  python -m coverage report -m
  ```

Os testes cobrem cenários de criação de objetos, integração com a API do GitHub e geração de logs, assegurando que as principais funcionalidades estejam sempre funcionando corretamente.

## 💡 Confiabilidade

A aplicação foi desenvolvida com foco em qualidade, clareza e robustez. A presença de testes automatizados e cobertura de código garante que as funcionalidades principais estejam protegidas contra regressões, tornando o projeto confiável tanto para uso pessoal quanto para colaboração aberta.

## 🤖 Apoio do GitHub Copilot

Todo o processo de automação, refino do script e organização do projeto foi realizado com o apoio do **GitHub Copilot**, mostrando como a IA pode potencializar a produtividade e criatividade de desenvolvedores.

## Commits padronizados com Commitizen

Este projeto utiliza o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) e a ferramenta Commitizen para garantir um histórico de commits limpo e automatizar o changelog.

**Como fazer um commit:**

1. Instale as dependências do projeto (inclui o Commitizen):
   ```sh
   pip install -r requirements.txt
   ```
2. Use o Commitizen para criar commits:
   ```sh
   C:/Python313/python.exe -m commitizen commit
   ```
   Siga o assistente interativo para escolher o tipo de commit e preencher a mensagem corretamente.

**Exemplo de mensagem válida:**
```
feat(docs): adiciona integração do Commitizen ao CI
```

Commits fora do padrão serão rejeitados pelo CI.

Para mais detalhes, consulte o arquivo `.cz.yaml` e a documentação do Commitizen.

## 👨‍💻 Sobre Mim

Sou um desenvolvedor focado em resolver problemas reais, começando pelas minhas próprias necessidades e compartilhando soluções que podem ajudar a comunidade. Se você também busca automatizar e melhorar seus fluxos de trabalho, fique à vontade para contribuir ou adaptar este projeto!

---

Feito com dedicação, mentalidade de melhoria contínua e atenção aos detalhes. 🚀
