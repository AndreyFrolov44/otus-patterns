from homework_2.command import MacroCommand
from homework_2.rotate import Rotate
from homework_4.commands.change_velocity import ChangeVelocityCommand
from homework_4.commands.check_velocity import CheckVelocityCommand
from homework_4.space_objects.movable_rotatable import MovableRotatableObject


class RotateChangeVelocityCommand(MacroCommand):
    def __init__(self, obj: MovableRotatableObject) -> None:
        self.commands = [CheckVelocityCommand(obj), Rotate(obj), ChangeVelocityCommand(obj)]
