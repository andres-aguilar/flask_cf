#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/saludar")
@app.route("/saludar/<nombre>")
@app.route("/saludar/<nombre>/<apellido>")
def saludar(nombre="Usuario", apellido=""):
    return "Saludos {0} {1}".format(nombre, apellido)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
