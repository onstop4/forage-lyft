from tires.tires import Tires


class Octoprime(Tires):
    def needs_service(self):
        return sum(self.tires) >= 3
