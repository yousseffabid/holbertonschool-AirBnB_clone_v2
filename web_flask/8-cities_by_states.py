#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ return all cities """
    states = storage.all(State).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


@app.teardown_appcontext
def teardown_data(exception):
    """
        reload  data
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
