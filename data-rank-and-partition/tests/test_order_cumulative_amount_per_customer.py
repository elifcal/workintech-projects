# pylint: disable-all
import os
import sqlite3
from nbresult import ChallengeResultTestCase

class TestOrderCumulativeAmountPerCustomer(ChallengeResultTestCase):
    db_path = os.path.join(os.path.dirname(__file__), '../data/ecommerce.sqlite')

    def query_db(self, query, *args):
        conn = sqlite3.connect(self.db_path)
        db = conn.cursor()
        db.execute(query, args)
        results = db.fetchall()
        return results

    def test_order_cumulative_amount_per_customer(self):
        result = self.query_db(self.result.query)
        result = [ (result[0], result[1], result[2], round(result[3], 1)) for result in result ]
        expected = [
            (1, 1, '2012-01-04', 48.0),
            (8, 1, '2012-06-13', 1989.7),
            (12, 1, '2012-09-13', 2021.7),
            (2, 2, '2012-01-27', 1948.7),
            (4, 2, '2012-03-13', 2348.7),
            (9, 2, '2012-07-06', 2648.7),
            (14, 2, '2012-10-29', 3529.7),
            (19, 2, '2013-02-21', 5156.2),
            (6, 3, '2012-04-28', 384.5),
            (10, 3, '2012-07-29', 517.7),
            (11, 3, '2012-08-21', 938.9),
            (16, 3, '2012-12-14', 1146.4),
            (18, 3, '2013-01-29', 1431.9),
            (20, 3, '2013-03-16', 1597.9),
            (3, 4, '2012-02-19', 2395.9),
            (5, 4, '2012-04-05', 6034.5),
            (7, 4, '2012-05-21', 7356.0),
            (15, 4, '2012-11-21', 8700.1),
            (13, 5, '2012-10-06', 250.0),
            (17, 5, '2013-01-06', 2192.6)
        ]
        self.assertIs(type(result), list)
        self.assertIs(type(result[0]), tuple)
        self.assertEqual(len(result), len(expected))
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[-1], expected[-1])
