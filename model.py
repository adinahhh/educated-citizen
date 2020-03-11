"""Models for final hackbright project """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Legislator(db.Model):
    """ Info on current legislators. """

    __tablename__ = "current_legislators"

    legislator_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    party = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    opensecrets_id = db.Column(db.Integer, nullable=False)
    govtrack_id = db.Column(db.Integer, nullable=False)
    votesmart_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """ provide info on legislator."""

        return f"Legislator: {self.full_name} party: {self.party}"

    # ask do I need to add more classes or if I can combine queries from
    # votesmart api and opensecrets api 
    # if i need to add more classes, then i need to add in backrefs
    # and foreign keys