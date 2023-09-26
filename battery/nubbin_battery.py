from battery.battery import Battery


class NubbinBattery(Battery):
    def needs_service(self):
        return (self.current_date - self.last_service_date).days > 4 * 365
