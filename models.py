class Repository:
    """
    Representa um repositório do GitHub.

    Attributes:
        name (str): Nome do repositório.
        url (str): URL do repositório.
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return f"Repository(name={self.name}, url={self.url})"
