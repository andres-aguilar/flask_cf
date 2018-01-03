from flask import Flask
from flask import request

app = Flask(__name__)
# Trabajando con parametros enviados por método GET


@app.route("/")
def index():
    return "Index"


@app.route("/saludo")
def saludo():
    # /saludo?nombre=Andres
    usuario = request.args.get("nombre", "Usuario")
    return "Saludos {0}".format(usuario)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
