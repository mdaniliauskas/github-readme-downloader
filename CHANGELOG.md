# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

## [1.1.0] - 2025-06-18
### Adicionado
- Geração automática de documentação com Sphinx, configurada para pt_BR.
- Docstrings Sphinx em todas as classes e métodos principais.
- Estrutura de documentação avançada: autodoc, autosummary, napoleon, doctest.
- Tema customizado sphinx_rtd_theme para documentação.
- Exemplo de log e relatório CSV gerados automaticamente.
- Dockerfile e instruções de uso com Docker.
- Integração com Coveralls e badge de cobertura.
- FAQ.md, API.md, CHANGELOG.md, CONTRIBUTING.md detalhados.
- Testes de documentação (doctest) integrados ao Sphinx.

### Corrigido
- Problemas de importação de módulos no Sphinx (ajuste em sys.path no conf.py).
- Ajustes em imports e modularização para compatibilidade com autodoc.

### Alterado
- Refatoração incremental para clean code, modularização e orientação a objetos.
- README.md expandido com exemplos, badges, instruções Docker, FAQ e API.

## [1.0.0] - 2025-06-17
### Adicionado
- Primeira versão pública com arquitetura orientada a objetos e modular.
- Testes automatizados e cobertura.
- Integração contínua com GitHub Actions.
- README completo e detalhado.
- Licença MIT.
- Guia de contribuição.
