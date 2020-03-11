""" File used to parse data from json to put into database """

from sqlalchemy import func
from model import Legislator

from model import connect_to_db, db
from server import app

def load_legislators():
    """ Load legislators from data file into database."""

    # ***ratings lab had a print statement, and then Class.query.delete()
    # because my data isnt changing, do I need to do this?

    # will need to correct file path below

    # need to download json file before i can decide how to parse data
    # for row in open("seed_data/")
    #     legislator_id
    #     full_name
    #     party
    #     url
    #     opensecrets_id
    #     govtrack_id
    #     votesmart_id

    #     legislator = Legislator(legislator_id=....)

        # adding to session to store it
        db.session.add(legislator)

    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # import data
    load_legislators()


