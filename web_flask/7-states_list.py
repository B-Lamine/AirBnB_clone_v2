#!/usr/bin/python3
""" Flask web app: a page listing of data in the database.
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """  template HTML response web page for data retrieved.
    """
    states_objs = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states_objs)


@app.teardown_appcontext
def teardown_db(exception):
    """ Close connection to db after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
