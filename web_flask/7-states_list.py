#!/usr/bin/python3
"""7-states_list Module"""
from flask import Flask, render_template
import models
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """Displays html page"""
    states = models.storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def appcontext_teardown(self):
    """use storage for fetching data from the storage engine
    """
    models.storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
