import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.now()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
