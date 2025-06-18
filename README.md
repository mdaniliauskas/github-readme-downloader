# 📚 GitHub Readme Downloader

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-API-black?logo=github)

## ✨ Motivação

Estou revisitando todos os repositórios do meu perfil no GitHub para:

- 🔍 Verificar quais repositórios possuem ou não um arquivo README.
- 📥 Baixar todos os READMEs disponíveis para análise local.
- 📝 Padronizar, reescrever e melhorar a documentação dos meus projetos.

Essa necessidade me levou a criar um script automatizado, que pode ser útil para qualquer pessoa que queira organizar e revisar seus próprios repositórios.

## 🚀 Sobre o Projeto

Este projeto automatiza o processo de:

1. Listar todos os repositórios públicos de um usuário do GitHub.
2. Baixar o arquivo README de cada repositório (tentando os ramos `main` e `master`).
3. Gerar um log detalhado com o status de cada repositório (README baixado ou não encontrado).
4. Permitir fácil adaptação para qualquer usuário do GitHub.

> **Mentalidade:** Resolvi um problema real do meu dia a dia, criando uma solução que pode ajudar outras pessoas a organizar e melhorar seus próprios projetos. Isso demonstra minha capacidade de identificar necessidades, automatizar tarefas e compartilhar conhecimento.

## 🛠️ Como Usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/mdaniliauskas/github-readme-downloader.git
   cd github-readme-downloader
   ```
2. **Instale as dependências:**
   ```bash
   pip install requests
   ```
3. **Execute o script:**
   ```bash
   python baixar_readmes.py
   ```
   - O script pedirá o nome de usuário do GitHub.
   - Os READMEs serão baixados na pasta `readmes` (ou na mesma pasta do script, conforme a versão).
   - Um log detalhado será gerado ao final do processo.

## 💡 Exemplos de Uso

- Revisar e padronizar a documentação dos seus projetos.
- Identificar rapidamente quais repositórios estão sem README.
- Automatizar tarefas repetitivas ligadas à documentação.

## 🤖 Apoio do GitHub Copilot

Todo o processo de automação, refino do script e organização do projeto foi realizado com o apoio do **GitHub Copilot**, mostrando como a IA pode potencializar a produtividade e criatividade de desenvolvedores.

## 👨‍💻 Sobre Mim

Sou um desenvolvedor focado em resolver problemas reais, começando pelas minhas próprias necessidades e compartilhando soluções que podem ajudar a comunidade. Se você também busca automatizar e melhorar seus fluxos de trabalho, fique à vontade para contribuir ou adaptar este projeto!

---

Feito com dedicação e mentalidade de melhoria contínua. 🚀
