from flask import Flask, render_template, request

from pprint import pformat
import os
import requests

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

API_KEY = os.environ['CIVIC_API_KEY']

@app.route('/')
def homepage():
    """ Homepage """

    return render_template('homepage.html')

@app.route('/search_results')
def search_results():

    return render_template('results.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')