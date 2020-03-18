""" File used to parse data from json to put into database """

from sqlalchemy import func
from model import Legislator

from legislators_current import legislature_json

from model import connect_to_db, db
from server import app
import json

# def load_legislators():
    # """ Load legislators from data file into database."""

    # ***ratings lab had a print statement, and then Class.query.delete()
    # because my data isnt changing, do I need to do this?
    # Legislator.query.delete()

    # full_name = []
    # party = []
    # govtrack_id = []

    # for legis in legislature_json:

    #     full_name.append(legis['name']['official_full'])
    #     party.append(legis['terms'][0]['party'])
    #     # opensecrets_id = legis['id']['opensecrets']
    #     govtrack_id.append(legis['id']['govtrack'])
    #     # votesmart_id = legis['id']['votesmart']

    #     legislator = Legislator(full_name=full_name, party=party, 
    #                             govtrack_id=govtrack_id)

    #     # adding to session to store it
    #     db.session.add(legislator)

    # db.session.commit()

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
        full_name = legislator_dict[i]['name']['official_full']
        party = legislator_dict[i]['terms'][0]['party']
        govtrack_id = legislator_dict[i]['id']['govtrack']
        i += 1
        
        legislator = Legislator(full_name=full_name, party=party, 
                                govtrack_id=govtrack_id)

        db.session.add(legislator)

    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # import data
    load_legislators()


