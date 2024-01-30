#!/usr/bin/python3
""" airbnb flask app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list states """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state)
    return render_template("7-states_list.html", states=state_list)


@app.teardown_appcontext
def close_teardown(error=None):
    """ close session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
