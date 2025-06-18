# Contributing to github-readme-downloader

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

## Como contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature ou correção (`git checkout -b minha-feature`)
3. Faça suas alterações e commit (`git commit -am 'feat: minha nova feature'`)
4. Dê push para a branch (`git push origin minha-feature`)
5. Abra um Pull Request

## Boas práticas
- Escreva código limpo e bem documentado
- Sempre adicione testes para novas funcionalidades
- Descreva claramente sua contribuição no Pull Request

## Commits padronizados

Para contribuir com este projeto, siga o padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/) utilizando a ferramenta Commitizen.

**Como criar um commit padronizado:**

1. Instale as dependências do projeto (inclui o Commitizen):
   ```sh
   pip install -r requirements.txt
   ```
2. Use o Commitizen para criar commits interativos:
   ```sh
   C:/Python313/python.exe -m commitizen commit
   ```
   Siga o assistente para preencher a mensagem corretamente.

**Exemplo de mensagem válida:**
```
feat(docs): adiciona instrução de commit padronizado
```

> Commits fora do padrão serão rejeitados pelo CI.

Consulte `.cz.yaml` e o README para mais detalhes.

Obrigado por ajudar a melhorar este projeto!
