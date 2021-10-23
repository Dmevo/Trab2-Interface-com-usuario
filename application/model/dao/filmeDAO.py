from application import filmes_lista

class FilmeDAO:

    def __init__(self):
        self.filmes_lista = filmes_lista

    def mostrar_filmes(self):
        return self.filmes_lista