# pylint: disable-all
import unittest

from farm.rice import Rice


class TestRice(unittest.TestCase):
    def setUp(self):
        self.rice = Rice()

    def test_initialize_grains_variable(self):
        self.assertEqual(self.rice.grains, 0,
                         "The `grains` instance variable should be initialized to 0")

    def test_water_method_exists(self):
        self.assertTrue(hasattr(Rice, 'water'),
                        "The `Rice` class should implement a `water` method")

    def test_water_method_adds_grains(self):
        self.rice.water()
        self.assertEqual(self.rice.grains, 5,
                         "The `water` method should add 5 grains")
        self.rice.water()
        self.assertEqual(self.rice.grains, 10,
                         "The `water` method should add 5 grains each time it is called")

    def test_ripe_method_exists(self):
        self.assertTrue(hasattr(Rice, 'ripe'),
                        "The `Rice` class should implement a `ripe` method")

    def test_ripe_method_behavior(self):
        self.assertFalse(self.rice.ripe(),
                         "The `ripe` method should return False when grains are less than 15")
        self.rice.grains = 15
        self.assertTrue(self.rice.ripe(),
                        "The `ripe` method should return True when grains are 15 or more")

    def test_transplant_method_exists(self):
        self.assertTrue(hasattr(Rice, 'transplant'),
                        "The `Rice` class should implement a `transplant` method")
