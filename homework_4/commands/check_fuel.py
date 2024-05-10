from dataclasses import dataclass
from homework_2.command import Command
from homework_4.exceptions import CommandException
from homework_4.space_objects.refueled import Refueled


@dataclass
class CheckFuelCommand(Command):
    _refueled: Refueled

    def execute(self) -> None:
        if self._refueled.get_fuel() - self._refueled.get_fuel_velocity() < 0:
            raise CommandException("Fuel is too low")
