#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from wtforms import Form, StringField, TextAreaField
from wtforms.fields.html5 import EmailField


class Formulario(Form):
    """ Clase Formulario """
    user = StringField("Usuario")
    email = EmailField("Email")
    comentario = TextAreaField("Comentario")


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    comment_form = Formulario()
    return render_template("formulario.html", form=comment_form)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
