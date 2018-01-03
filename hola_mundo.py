from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola mundo"


app.run(port=8080, debug=True)
