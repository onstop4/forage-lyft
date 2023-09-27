from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self, tires):
        self.tires = tires

    @abstractmethod
    def needs_service(self):
        pass
