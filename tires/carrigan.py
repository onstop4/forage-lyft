from tires.tires import Tires


class Carrigan(Tires):
    def needs_service(self):
        return any(tire_wear >= 0.9 for tire_wear in self.tires)
