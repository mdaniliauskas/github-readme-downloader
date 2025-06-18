class Repository:
    """Representa um repositório do GitHub."""
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return f"Repository(name={self.name}, url={self.url})"
