from flask import Flask
import os
from application.model.entity.filme import Filme

app = Flask(__name__, static_folder = os.path.abspath("application/view/static"), template_folder = os.path.abspath("application/view/templates"))

filmes_lista = [Filme(1, "Shang-Chi e a Lenda dos Dez Aneis", "shang chi.jpg", "02h 12m", "faixa-etaria-12.png", ["20:30","22:30"], "02/09/21"),
                Filme(2, "O Esquadrão Suicida", "esquadrão suicida.jpg", "02h 12m", "img.jpg", ["20:30", "22:30"], "05/08/21"),
                Filme(3, "Pedro Coelho 2: O Fugitivo", "pedro_coelho.jpg", "1h 33m", "img.jpg", ["16:30","17:30"], "26/08/21"),
                Filme(4, "O Poderoso Chefinho 2 - Negócios da Família", "o_poderoso_chefinho.jpg", "1h 47m", "img.jpg", ["15:40", "16:40"], "12/08/21")]

from application.controller import home_controller