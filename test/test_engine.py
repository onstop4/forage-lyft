import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapulet(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = CapuletEngine(datetime.today(), 30001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = CapuletEngine(datetime.today(), 0, 0)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(datetime.today(), True)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = SternmanEngine(datetime.today(), False)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = WilloughbyEngine(datetime.today(), 60001, 0)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = WilloughbyEngine(datetime.today(), 0, 0)
        self.assertFalse(engine.needs_service())
