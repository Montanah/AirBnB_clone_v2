#!/usr/bin/python3
'''
a script that starts a Flask web app
'''

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    '''
        returns an HTML list of states
    '''
    all_states = list(storage.all('State').values())
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def close_storage(error):
    '''
        closes storage
    '''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
