#!/usr/bin/python3
""" Minimalist Flask web app
"""


from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Index web page response.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB response web page.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text=''):
    """ C_is_fun response web page.
    """
    if '_' in text:
        tmp_list = [c if c != '_' else ' ' for c in list(text)]
        text = ''.join(tmp_list)
    return "C {}".format(escape(text))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def pythonisfun(text='is cool'):
    """ Python_is_fun response web page.
    """
    if '_' in text:
        tmp_list = [c if c != '_' else ' ' for c in list(text)]
        text = ''.join(tmp_list)
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """  Response web page only for numbers (int).
    """
    return "{} is a number".format(escape(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
