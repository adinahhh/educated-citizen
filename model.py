"""Models for final hackbright project """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

class Legislator(db.Model):
    """ Info on current legislators. """

    __tablename__ = "current_legislators"

    legislator_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    party = db.Column(db.String(50), nullable=False)
    opensecrets_id = db.Column(db.String(10), nullable=True)
    govtrack_id = db.Column(db.Integer, nullable=False)
    votesmart_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        """ provide info on legislator."""

        return f"Legislator: {self.full_name} party: {self.party}"


def connect_to_db(app):
    """ Connect database to Flask app."""

    # Configure to use my PstgreSQL database
    # ***come back to this to make sure db name is correct ***
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///legislature'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # if I run this module interactively, it will leave
    # me in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    # create tables
    db.create_all()