#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
import models
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """return an html page with list of states"""
    return render_template('9-states.html',
                           states=models.storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """return an html page with the state based on given id"""
    for state in models.storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html',
                                   states=state, correct_id=1)
    return render_template("9-states.html", correct_id=0)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
