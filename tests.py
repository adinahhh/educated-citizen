import unittest

from server import app
from model import db, Legislator, connect_to_db

class Tests(unittest.TestCase):
    """ Tests routes for educated citizen app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage_route(self):
        """ tests homepage route returns correct HTML."""

        result = self.client.get('/')
        self.assertIn(b'elected official', result.data)

    def test_officials_route(self):
        """ tests route that finds elected officials based on zip code."""

        result = self.client.get("/officials")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<h3>Your Elected Officials:</h3>', result.data)

    def test_search_contributions_official(self):
        """For search page that asks for last name and state for contrib info"""

        result = self.client.get("/search")
        self.assertIn(b'<label>Please enter legislator\'s last name:</label>',
                      result.data)

    # def test_contributions_member_route(self):
    #     """ Tests page that shows all contribution info for a legislator """

    #     result = self.client.get("/search-results", query_string={"last_name": "Omar", "state": "MN"})
    #     self.assertIn(b'<h4>Legislator\'s Contributions by Industry:</h4>', result.data)
    #     self.assertEqual(result.status_code, 200)

    def test_votes_by_issue_route(self):
        """ This tests search page for legislator's voting records. """

        result = self.client.get('votes-by-topic')
        self.assertIn(b'<label>Please enter legislator\'s last name:</label>', result.data)

    # def test_voting_record_results(self):
    #     """ For the page of results of a legislator's previous votes """

    #     result = self.client.get('official-votes')
    #     self.assertIn(b'Voting records information', result.data)
    #     self.assertEqual(result.status_code, 200)


# class TestingMyDatabase(unittest.TestCase):
#     """ Flask test that use my database. """

#     def setUp(self):
#         """Stuff to do before every test."""

#         self.client = app.test_client()
#         app.config['TESTING'] = True

#         # Connect to test database (uncomment when testing database)
#         connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add in data (uncomment when testing database)
#         db.create_all()
#         example_data()

#     def tearDown(self):
#     """Do at end of every test."""

#         # (uncomment when testing database)
#         db.session.close()
#         db.drop_all()

#     def test_legis_database(self):

if __name__ == "__main__":
    unittest.main()