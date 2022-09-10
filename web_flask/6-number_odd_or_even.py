#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def just_HBNB():
    """Display HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display text"""

    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display text"""

    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_integer(n):
    """Display integer"""

    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display html page only if <n> is an integer"""

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display html page only if <n> is an integer"""

    if n % 2 == 0:
        res = "even"
    else:
        res = "odd"
    return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
