from homework_2.command import MacroCommand
from homework_2.move import Move
from homework_4.commands.burn_fuel import BurnFuelCommand
from homework_4.commands.check_fuel import CheckFuelCommand
from homework_4.space_objects.movable_refueled import MovableRefueledObject


class CheckBurnFuelMoveCommand(MacroCommand):
    def __init__(self, obj: MovableRefueledObject) -> None:
        self.commands = [CheckFuelCommand(obj), Move(obj), BurnFuelCommand(obj)]
