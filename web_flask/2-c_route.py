#!/usr/bin/python3
""" First flask app """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """ url variables """
    var_str = text.replace('_', ' ')
    return "C {}".format(escape(var_str))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
