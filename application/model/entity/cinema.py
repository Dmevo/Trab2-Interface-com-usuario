class Cinema:

    def __init__(self, nome=None, sala=None, filme=None):
        self.nome = nome
        self.sala = sala
        self.filme = filme

    def get_nome(self):
        return self.nome

    def get_sala(self):
        return self.sala

    def get_filme(self):
        return self.filme