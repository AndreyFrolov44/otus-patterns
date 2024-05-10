from dataclasses import dataclass
from homework_2.command import Command
from homework_4.space_objects.refueled import Refueled


@dataclass
class BurnFuelCommand(Command):
    _refueled: Refueled

    def execute(self) -> None:
        self._refueled.set_fuel(self._refueled.get_fuel() - self._refueled.get_fuel_velocity())
