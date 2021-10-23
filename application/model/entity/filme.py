class Filme:
    
    def __init__(self, id=None, titulo=None, cartaz=None, duracao=None, faixa_etaria=None, horarios=None, lancamento=None):
        self.id = id
        self.titulo = titulo
        self.cartaz = cartaz
        self.duracao = duracao
        self.faixa_etaria = faixa_etaria
        self.horarios = horarios
        self.lancamento = lancamento

    def get_id(self):
        return self.id

    def get_titulo(self):
        return self.titulo

    def get_cartaz(self):
        return self.cartaz

    def get_duracao(self):
        return self.duracao

    def get_faixa_etaria(self):
        return self.faixa_etaria

    def get_horarios(self):
        return self.horarios
    
    def get_lancamento(self):
        return self.lancamento