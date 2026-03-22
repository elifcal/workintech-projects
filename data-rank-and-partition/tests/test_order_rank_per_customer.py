# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestOrderRankPerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_order_rank_per_customer(self):
        result = self.query_db(self.result.query)
        expected = [
            (1, 1, '2012-01-04', 1),
            (8, 1, '2012-06-13', 2),
            (12, 1, '2012-09-13', 3),
            (2, 2, '2012-01-27', 1),
            (4, 2, '2012-03-13', 2),
            (9, 2, '2012-07-06', 3),
            (14, 2, '2012-10-29', 4),
            (19, 2, '2013-02-21', 5),
            (6, 3, '2012-04-28', 1),
            (10, 3, '2012-07-29', 2),
            (11, 3, '2012-08-21', 3),
            (16, 3, '2012-12-14', 4),
            (18, 3, '2013-01-29', 5),
            (20, 3, '2013-03-16', 6),
            (3, 4, '2012-02-19', 1),
            (5, 4, '2012-04-05', 2),
            (7, 4, '2012-05-21', 3),
            (15, 4, '2012-11-21', 4),
            (13, 5, '2012-10-06', 1),
            (17, 5, '2013-01-06', 2)
        ]
        self.assertIs(type(result), list)
        self.assertIs(type(result[0]), tuple)
        self.assertEqual(len(result), len(expected))
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[-1], expected[-1])
