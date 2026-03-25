# pylint: disable=missing-docstring
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestQueryOrders(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_length_list(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 20)

    def test_first_element(self):
        results = self.query_db(self.result.query)
        result_0 = results[0]
        expected = (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75)
        self.assertEqual(result_0, expected)
