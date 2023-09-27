from car import Car

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class CarFactory:
    @staticmethod
    def create_calliope(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_array,
    ):
        return Car(
            CapuletEngine(last_service_date, current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
            Carrigan(tire_array),
        )

    @staticmethod
    def create_glissade(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_array,
    ):
        return Car(
            WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
            Carrigan(tire_array),
        )

    @staticmethod
    def create_palindrome(
        current_date, last_service_date, warning_light_on, tire_array
    ):
        return Car(
            SternmanEngine(last_service_date, warning_light_on),
            SpindlerBattery(last_service_date, current_date),
            Carrigan(tire_array),
        )

    @staticmethod
    def create_rorschach(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_array,
    ):
        return Car(
            WilloughbyEngine(last_service_date, current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
            Octoprime(tire_array),
        )

    @staticmethod
    def create_thovex(
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_array,
    ):
        return Car(
            CapuletEngine(last_service_date, current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
            Octoprime(tire_array),
        )
