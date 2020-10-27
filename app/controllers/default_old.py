from app import app

@app.route("/index")
@app.route ("/")
def index():
    return "Hello World!"

""" @app.route("/teste")
def teste():
    return "ola"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def test(name=None):
    #return "olá, %s!" % name
    if name:
        return "ola, %s" % name
    else:
        return "Olá, usuario"
 """