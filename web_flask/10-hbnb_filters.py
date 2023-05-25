#!/usr/bin/python3
''' A script that starts a Flask web app for HBNB '''

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb():
    ''' returns HBNB index page '''
    all_states = list(storage.all('State').values())
    all_cities = list(storage.all('City').values())
    states_cities = ({state:
                      [city for city in all_cities
                       if city.state_id == state.id]
                      for state in all_states})
    all_amenities = list(storage.all('Amenity').values())
    return render_template('10-hbnb_filters.html',
                           states_cities=states_cities,
                           amenities=all_amenities)


@app.teardown_appcontext
def close_storage(error):
    ''' closes out storage '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
