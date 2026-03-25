# pylint: disable-all
import unittest

from farm.corn import Corn


class TestCorn(unittest.TestCase):
    def setUp(self):
        self.corn = Corn()

    def test_initialize_grains_variable(self):
        self.assertEqual(self.corn.grains, 0,
                         "The `grains` instance variable should be initialized to 0")

    def test_water_method_exists(self):
        self.assertTrue(hasattr(Corn, 'water'),
                        "The `Corn` class should implement a `water` method")

    def test_water_method_adds_grains(self):
        self.corn.water()
        self.assertEqual(self.corn.grains, 10,
                         "The `water` method should add 10 grains")
        self.corn.water()
        self.assertEqual(self.corn.grains, 20,
                         "The `water` method should add 10 grains each time it is called")

    def test_ripe_method_exists(self):
        self.assertTrue(hasattr(Corn, 'ripe'),
                        "The `Corn` class should implement a `ripe` method")

    def test_ripe_method_behavior(self):
        self.assertFalse(self.corn.ripe(),
                         "The `ripe` method should return False when grains are less than 15")
        self.corn.grains = 15
        self.assertTrue(self.corn.ripe(),
                        "The `ripe` method should return True when grains are 15 or more")
