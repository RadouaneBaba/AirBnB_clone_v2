#!/usr/bin/python3
""" airbnb flask app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """ list states """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state)
    return render_template("8-cities_by_states.html", states=state_list)


@app.teardown_appcontext
def close_teardown(error=None):
    """ close session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
