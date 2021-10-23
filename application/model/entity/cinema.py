class Cinema:

    def __init__(self, nome=None, sala=None, tipo=None):
        self.nome = nome
        self.sala = sala
        self.tipo = tipo

    def get_nome(self):
        return self.nome

    def get_sala(self):
        return self.sala

    def get_tipo(self):
        return self.tipo