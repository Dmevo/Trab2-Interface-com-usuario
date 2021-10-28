class Cinema:

    def __init__(self, nome=None, sala=None):
        self.nome = nome
        self.sala = sala

    def get_nome(self):
        return self.nome

    def get_sala(self):
        return self.sala