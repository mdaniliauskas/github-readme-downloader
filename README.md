# 📚 GitHub Readme Downloader

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-API-black?logo=github)
![tqdm](https://img.shields.io/badge/tqdm-barra%20de%20progresso-green)

## ✨ Motivação

Estou revisitando todos os repositórios do meu perfil no GitHub para:

- 🔍 Verificar quais repositórios possuem ou não um arquivo README.
- 📥 Baixar todos os READMEs disponíveis para análise local.
- 📝 Padronizar, reescrever e melhorar a documentação dos meus projetos.

Essa necessidade me levou a criar um script automatizado, que pode ser útil para qualquer pessoa que queira organizar e revisar seus próprios repositórios.

## 🚀 Sobre o Projeto

Este projeto automatiza o processo de:

1. Listar todos os repositórios públicos de um usuário do GitHub.
2. Baixar o arquivo README de cada repositório (tentando diferentes variações de nome e branch, como `README.md`, `Readme.md`, etc, nos ramos `main` e `master`).
3. Gerar um log detalhado e organizado, separando repositórios com e sem README, incluindo as URLs para fácil acesso.
4. Exibir uma barra de progresso visual durante o processo.
5. Permitir fácil adaptação para qualquer usuário do GitHub, inclusive via argumentos de linha de comando.
6. Tratar erros de rede, usuário inexistente e limitações de API.

> **Mentalidade:** Resolvi um problema real do meu dia a dia, criando uma solução que pode ajudar outras pessoas a organizar e melhorar seus próprios projetos. Isso demonstra minha capacidade de identificar necessidades, automatizar tarefas e compartilhar conhecimento.

## 🛠️ Como Usar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/mdaniliauskas/github-readme-downloader.git
   cd github-readme-downloader
   ```
2. **Instale as dependências:**
   ```bash
   pip install requests tqdm
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

## 💡 Funcionalidades

- Organização do código em funções e uso de argparse.
- Barra de progresso com tqdm.
- Logging estruturado e tratamento de exceções.
- Checagem de README em diferentes variações de nome e branch.
- Delay configurável entre requisições para evitar rate limit.
- Mensagem clara caso o usuário não exista.
- Log final separado e visual para facilitar ações futuras.

## 🤖 Apoio do GitHub Copilot

Todo o processo de automação, refino do script e organização do projeto foi realizado com o apoio do **GitHub Copilot**, mostrando como a IA pode potencializar a produtividade e criatividade de desenvolvedores.

## 👨‍💻 Sobre Mim

Sou um desenvolvedor focado em resolver problemas reais, começando pelas minhas próprias necessidades e compartilhando soluções que podem ajudar a comunidade. Se você também busca automatizar e melhorar seus fluxos de trabalho, fique à vontade para contribuir ou adaptar este projeto!

---

Feito com dedicação, mentalidade de melhoria contínua e atenção aos detalhes. 🚀
