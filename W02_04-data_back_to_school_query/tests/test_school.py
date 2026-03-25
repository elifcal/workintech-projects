# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestSchool(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/school.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_paris(self):
        results = self.query_db(self.result.query, 'Paris')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 5)

    def test_london(self):
        results = self.query_db(self.result.query, 'London')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_berlin(self):
        results = self.query_db(self.result.query, 'Berlin')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 2)

    def test_brussels(self):
        results = self.query_db(self.result.query, 'Brussels')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 1)

    def test_barcelona(self):
        results = self.query_db(self.result.query, 'Barcelona')
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)
