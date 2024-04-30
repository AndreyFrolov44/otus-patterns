from dataclasses import dataclass


class Refueled:
    def get_fuel(self):
        raise NotImplementedError()

    def set_fuel(self, fuel: int):
        raise NotImplementedError()

    def get_fuel_velocity(self):
        raise NotImplementedError()


@dataclass
class RefueledObject(Refueled):
    fuel: int
    fuel_velocity: int

    def get_fuel(self):
        return self.fuel

    def set_fuel(self, fuel: int):
        if fuel >= 0:
            self.fuel = fuel
        else:
            self.fuel = 0

    def get_fuel_velocity(self):
        return self.fuel_velocity
