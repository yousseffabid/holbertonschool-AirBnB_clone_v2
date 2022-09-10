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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """return an html page with list of states"""
    return render_template('8-cities_by_states.html',
                           states=models.storage.all(State))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
