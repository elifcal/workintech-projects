# pylint: disable-all
import unittest

from farm.crop import Crop
from farm.corn import Corn
from farm.rice import Rice

class TestCrop(unittest.TestCase):
    def setUp(self):
        self.crop = Crop()

    def test_initialize_grains_variable(self):
        self.assertEqual(self.crop.grains, 0,
                         "The `grains` instance variable should be initialized to 0")

    def test_ripe_method_exists(self):
        self.assertTrue(hasattr(Crop, 'ripe'),
                        "The `Crop` class should implement a `ripe` method")

    def test_ripe_method_behavior(self):
        self.assertFalse(self.crop.ripe(),
                         "The `ripe` method should return False when grains are less than 15")
        self.crop.grains = 15
        self.assertTrue(self.crop.ripe(),
                        "The `ripe` method should return True when grains are 15 or more")


class TestCornInheritance(unittest.TestCase):
    def test_corn_inherits_from_crop(self):
        self.assertTrue(issubclass(Corn, Crop), "`Corn` should inherit from `Crop`")

    def test_corn_does_not_duplicate_crop_methods(self):
        self.assertNotIn('ripe', Corn.__dict__,
                         "`Corn` should not duplicate the `ripe` method from `Crop`")
        self.assertNotIn('__init__', Corn.__dict__,
                         "`Corn` should not duplicate the `__init__` method from `Crop`")


class TestRiceInheritance(unittest.TestCase):
    def test_rice_inherits_from_crop(self):
        self.assertTrue(issubclass(Rice, Crop), "`Rice` should inherit from `Crop`")

    def test_rice_does_not_duplicate_crop_methods(self):
        self.assertNotIn('ripe', Rice.__dict__,
                         "`Rice` should not duplicate the `ripe` method from `Crop`")
        self.assertNotIn('__init__', Rice.__dict__,
                         "`Rice` should not duplicate the `__init__` method from `Crop`")
