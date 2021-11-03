from application import filmes_lista
from application import breve_lista

class FilmeDAO:

    def __init__(self):
        self.filmes_lista = filmes_lista
        self.breve_lista = breve_lista

    def mostrar_filmes(self):
        return self.filmes_lista

    def mostrar_breve(self):
        return self.breve_lista