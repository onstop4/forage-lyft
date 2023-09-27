import unittest

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = Carrigan([0.9, 0, 0, 0])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = Carrigan([0.8, 0, 0, 0])
        self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self):
        tires = Octoprime([1, 1, 1, 0])
        self.assertTrue(tires.needs_service())

    def test_should_not_be_serviced(self):
        tires = Octoprime([1, 1, 0, 0])
        self.assertFalse(tires.needs_service())
