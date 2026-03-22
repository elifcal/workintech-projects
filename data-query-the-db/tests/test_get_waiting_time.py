# pylint: disable=missing-docstring
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestGetWaitingTime(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_size_list(self):
        results = self.query_db(self.result.query)
        self.assertEqual(len(results), 20)

    def test_type_results(self):
        results = self.query_db(self.result.query)
        self.assertIsInstance(results, list)

    def test_first_result(self):
        results = self.query_db(self.result.query)
        expected = \
            (1, 1, 1, '2012-01-04', '2012-01-09', '2012-01-05', 1, 3.75, 1.0)
        self.assertEqual(results[0], expected)

    def test_last_result(self):
        results = self.query_db(self.result.query)
        expected = \
            (19, 2, 4, '2013-02-21', '2013-02-26', '2013-03-01', 4, 14.0, 8.0)
        self.assertEqual(results[len(results) - 1], expected)
