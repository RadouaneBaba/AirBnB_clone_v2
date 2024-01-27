#!/usr/bin/python3
""" First flask app """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def hello_hbnb():
    """ hello hbnb """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0") 
