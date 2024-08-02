#!/usr/bin/python3
""" Flask web app: a page listing of data in the database.
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """  template HTML response web page for data retrieved.
    """
    states_objs = list(storage.all(State).values())
    amenities_objs = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states=states_objs,
                           amenities=amenities_objs)


@app.teardown_appcontext
def teardown_db(exception):
    """ Close connection to db after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
