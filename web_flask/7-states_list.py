#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
import models
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """return an html page with list of states"""
    return render_template('7-states_list.html',
                           states=models.storage.all(State))


@app.teardown_appcontext
def close_sqlalchemy_sess(exception):
    """remove the current SQLAlchemy Session"""
    models.storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
