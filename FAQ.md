# FAQ - github-readme-downloader

**1. O script não encontra alguns READMEs, mesmo eles existindo. O que pode ser?**
- O script tenta várias variações de nome (README.md, Readme.md, etc) e nos ramos main/master. Se o README estiver em outro branch ou com nome diferente, ele não será encontrado.

**2. O script parou por limite de requisições. O que fazer?**
- A API do GitHub tem limites de requisições para usuários não autenticados. Aguarde alguns minutos ou reduza o delay entre as requisições.

**3. Como rodar o script para outro usuário do GitHub?**
- Basta informar o nome de usuário ao rodar o script ou usar o argumento `-u`.

**4. Como acessar os arquivos baixados e relatórios usando Docker?**
- Use o parâmetro `-v` para mapear volumes, conforme instruções no README.

**5. O script funciona com repositórios privados?**
- Não, apenas repositórios públicos são suportados nesta versão.

**6. Como contribuir ou sugerir melhorias?**
- Veja o arquivo CONTRIBUTING.md para orientações.
