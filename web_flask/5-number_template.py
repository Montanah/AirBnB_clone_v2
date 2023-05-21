#!/usr/bin/python3
'''
a script that starts a Flask web app
'''

from flask import Flask, render_template


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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
        displays route with text variable
    '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is cool'):
    '''
        displays route with optional variable
    '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    '''
        displays route testing if input is an int
    '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    '''
        route showing html page if input is int
    '''
    return render_template('5-number.html', number=str(n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
