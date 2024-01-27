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
def c_is_fun(text):
    """ url variables """
    var_str = text.replace('_', ' ')
    return "C {}".format(escape(var_str))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_cool(text="is cool"):
    """ default url variable """
    py_str = text.replace('_', ' ')
    return "Python {}".format(escape(py_str))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ integer variable """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
