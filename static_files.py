#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("archivos_estaticos.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
