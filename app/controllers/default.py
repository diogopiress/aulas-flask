from flask import render_template #precisa importar este modulo para pegar o html
from app import app


@app.route("/index/<user>")
@app.route ("/", defaults = {"user":None})
def index(user):
    return render_template('base.html', user=user)