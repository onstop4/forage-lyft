from battery.battery import Battery


class SpindlerBattery(Battery):
    def needs_service(self):
        return (self.current_date - self.last_service_date).days > 2 * 365
