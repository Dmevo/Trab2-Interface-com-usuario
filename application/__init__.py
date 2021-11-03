from flask import Flask
import os
from application.model.entity.filme import Filme
from application.model.entity.cinema import Cinema

app = Flask(__name__, static_folder = os.path.abspath("application/view/static"), template_folder = os.path.abspath("application/view/templates"))

filmes_lista = [Filme(1, "Shang-Chi e a Lenda dos Dez Aneis", "shang chi.jpg", "02h 12m", "faixa-etaria-12.png", ["20:30","22:30"], "02/09/21", ["2D", "LEG"]),
                Filme(2, "O Esquadrão Suicida", "esquadrão suicida.jpg", "02h 12m", "faixa-etaria-16.png", ["20:30", "22:30"], "05/08/21", ["2D", "LEG"])]

cinemas_lista = [Cinema("Cinemaxx Pátio Casario Vassouras", "Sala 1")]

breve_lista = [Filme(3, "Pedro Coelho 2: O Fugitivo", "pedro_coelho.jpg", "1h 33m", "faixa-etaria-livre.png", ["16:30","17:30"], "26/08/21", ["3D", "DUB"]),
                Filme(4, "O Poderoso Chefinho 2 - Negócios da Família", "o_poderoso_chefinho.jpg", "1h 47m", "faixa-etaria-livre.png", ["15:40", "16:40"], "12/08/21", ["3D", "DUB"])]



from application.controller import home_controller