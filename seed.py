""" File used to parse data from json to put into database """

from sqlalchemy import func
from model import Legislator

from legislators_current import legislature_json

from model import connect_to_db, db
from server import app
import json


def json_reader(file_path):
    """ open and loads json files """

    with open(file_path) as file:
        json_dict = json.load(file)

    return json_dict

def load_legislators():
    """ load legislators from json file into db"""

    print('Legislator')

    Legislator.query.delete()

    legislator_file = "seed_data/legislators-current.json"

    legislator_dict = json_reader(legislator_file)

    i = 0

    for key in legislator_dict:
        last_name = legislator_dict[i]['name']['last'].upper()
        full_name = legislator_dict[i]['name']['official_full']
        state = legislator_dict[i]['terms'][0]['state']
        party = legislator_dict[i]['terms'][0]['party']
        opensecrets_id = legislator_dict[i]['id'].get('opensecrets', None)
        govtrack_id = legislator_dict[i]['id']['govtrack']
        votesmart_id = legislator_dict[i]['id'].get('votesmart', None)
        phone = legislator_dict[i]['terms'][-1].get('phone', None)
        website = legislator_dict[i]['terms'][-1].get('rss_url', None)
        i += 1

        legislator = Legislator(last_name=last_name, full_name=full_name,
                                state=state, party=party,
                                opensecrets_id=opensecrets_id,
                                govtrack_id=govtrack_id,
                                votesmart_id=votesmart_id, phone=phone,
                                website=website)

        db.session.add(legislator)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # import data
    load_legislators()


