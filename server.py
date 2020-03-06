from flask import Flask, render_template, request

from pprint import pformat
import os
import requests

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

API_KEY = os.environ['CIVIC_API_KEY']

@app.route('/')
def homepage():
    """ Homepage with user form"""

    return render_template('homepage.html')

@app.route('/search')
def search_address():
    """User search for ballot with street address """

# below is for electionQuery
    election_url = 'https://www.googleapis.com/civicinfo/v2/elections'
    election_payload = {'key' : API_KEY}

    election_response = requests.get(election_url, params=election_payload)

    election_data = election_response.json()
    # here i need to figure out how to queue my data
    elections = election_data['elections']

    return render_template('results.html', elections=elections)

# below is for voterInfoQuery
# match address from homepage.html with address in payload
    # voter_address = request.args.get('address', '')

# use elections id from election query as a param in voter_payload
# will the electionid be stored in a session key?

    # voter_url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    # voter_payload = {'key' : API_KEY, 'voter_address': address, 'electionId' : '2000'}
    # voter_response = requests.get(voter_url, params=voter_payload)
    # voter_info_json = voter_response.json() 


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')