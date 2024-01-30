#!/usr/bin/python3
""" airbnb flask app """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters_list():
    """ list states """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state)

    amenities = storage.all(Amenity)
    amenity_list = []
    for amenity in amenities.values():
        amenity_list.append(amenity)
    return render_template("10-hbnb_filters.html",
                           states=state_list,
                           amenities=amenity_list)


@app.teardown_appcontext
def close_teardown(error=None):
    """ close session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
