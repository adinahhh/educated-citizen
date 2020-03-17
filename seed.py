""" File used to parse data from json to put into database """

from sqlalchemy import func
from model import Legislator

from legislators_current import legislature_json

from model import connect_to_db, db
from server import app

def load_legislators():
    """ Load legislators from data file into database."""

    # ***ratings lab had a print statement, and then Class.query.delete()
    # because my data isnt changing, do I need to do this?


    for legis in legislature_json:

        full_name = legis['name']['official_full']
        party= legis['terms'][0]['party']
        opensecrets_id = legis['id']['opensecrets']
        govtrack_id = legis['id']['govtrack']
        # votesmart_id = legis['id']['votesmart']

        legislator = Legislator(full_name=full_name, party=party, 
                                opensecrets_id=opensecrets_id,
                                govtrack_id=govtrack_id)

        # adding to session to store it
        db.session.add(legislator)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # import data
    load_legislators()


