from application import cinemas_lista

class CinemaDAO:

    def __init__(self):
        self.cinemas_lista = cinemas_lista

    def mostrar_cinemas(self):
        return self.cinemas_lista