#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display /c/<text>"""
    return 'C ' + text.replace('_' + ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """display /python/<text>"""
    return 'python ' + text.replace('_' + ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
