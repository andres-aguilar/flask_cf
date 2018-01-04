#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    lista = list(range(0, 9))
    return render_template("herencia.html", lista=lista)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
