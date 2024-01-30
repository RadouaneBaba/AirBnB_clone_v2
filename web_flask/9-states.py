#!/usr/bin/python3
""" airbnb flask app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """ list states """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state)
    return render_template("9-states.html", states=state_list, state_search=False)


@app.route("/states/<state_id>", strict_slashes=False)
def state_id(state_id):
    """ list id state """
    states = storage.all(State)
    state_dict = None
    for state in states.values():
        if state.id == state_id:
            state_dict = state
    return render_template("9-states.html", state=state_dict, state_search=True)


@app.teardown_appcontext
def close_teardown(error=None):
    """ close session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
