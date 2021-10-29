from flask import render_template
from application import app
from application.model.dao.filmeDAO import FilmeDAO
from application.model.dao.cinemaDAO import CinemaDAO

@app.route('/')
def index():
    filme_dao = FilmeDAO()
    filme_lista = filme_dao.mostrar_filmes()

    return render_template("home.html", filme_lista = filme_lista)

@app.route('/detalhe/<id>')
def detalhe(id):
    filme_dao = FilmeDAO()
    filme_lista = filme_dao.mostrar_filmes()
    cinema_dao = CinemaDAO()
    cinema_lista = cinema_dao.mostrar_cinemas()
    for filme in filme_lista:
        if str(filme.get_id()) == id:
            return render_template("detalhe.html", filme = filme, cinema_lista = cinema_lista)

@app.route('/conta')
def conta():
    return render_template("conta.html")