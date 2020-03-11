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

@app.route('/elections')
def election_info():
    """ election query info, unsure if i will use this """

# below is for electionQuery
    election_url = 'https://www.googleapis.com/civicinfo/v2/elections'
    election_payload = {'key' : API_KEY}

    election_response = requests.get(election_url, params=election_payload)

    # response in json
    election_data = election_response.json()
    election_info_data = election_data['elections']

    # converting dict into list, getting back election name & date
    elections_list = list(election_info_data[0].values())
    elections = elections_list[1:3]


    return render_template('results.html', elections=elections)

    # remember the electionId is the first value in the list for elections

@app.route('/contests')
def contest_info():
    """User search for ballot with street address """

# below is for voterInfoQuery
# match address from homepage.html with address in payload
    address = request.args.get('address', '')

# use elections id from election query as a param in voter_payload
# will the electionid be stored in a session key?

    voter_url = 'https://www.googleapis.com/civicinfo/v2/voterinfo'
    voter_payload = {'key' : API_KEY, 'address': address}
    voter_response = requests.get(voter_url, params=voter_payload)
    voter_info_json = voter_response.json()

    # getting election data, converting to list
    voter_election_data = voter_info_json['election']
    voter_election_list = list(voter_election_data.values())
    elections = voter_election_list[1:3] 

    # unsure how to get values from contests without indexing
    # contests[0] gives info about first office contest
    first_contest_data = voter_info_json['contests'][0]
    first_contest_list = [(key,value) for key, value in first_contest_data.items()]
    spliced_data = first_contest_list[1:4:2]

    candidate_info = first_contest_list[7][1:]


    return render_template('ballot.html', elections=elections, 
                           contests=spliced_data, candidates=candidate_info)



@app.route('/smartvote')
def vote_smart():
    """ Trying new stuff with Vote Smart API"""
    pass

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')