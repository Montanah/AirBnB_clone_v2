#!/usr/bin/python3
'''
a script that starts a Flask web app
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''
        tests basic flask app
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''
        tests basic flask app with /hbnb path
    '''
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
