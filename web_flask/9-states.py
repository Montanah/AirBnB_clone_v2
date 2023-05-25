#!/usr/bin/python3
''' a script that starts a Flask web app '''

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    ''' returns an HTML list of states with cities inside each state '''
    all_states = list(storage.all('State').values())
    all_cities = list(storage.all('City').values())
    states_cities = ({state:
                      [city for city in all_cities
                       if city.state_id == state.id]
                      for state in all_states})
    return render_template('8-cities_by_states.html',
                           states_cities=states_cities)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def one_state(id=None):
    ''' returns a HTML list of cities in a single state '''
    if id is None:
        all_states = list(storage.all('State').values())
        return render_template('7-states_list.html', all_states=all_states)
    all_states = storage.all('State')
    all_cities = list(storage.all('City').values())
    try:
        my_state = all_states['State.{}'.format(id)]
    except Exception:
        return render_template('9-states.html', state=None, cities=None)
    my_cities = [city for city in all_cities if city.state_id == my_state.id]
    return render_template('9-states.html', state=my_state, cities=my_cities)


@app.teardown_appcontext
def close_storage(error):
    ''' closes storage '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
