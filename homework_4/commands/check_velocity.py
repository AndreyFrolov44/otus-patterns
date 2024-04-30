from dataclasses import dataclass
from homework_2.command import Command
from homework_2.move import Movable
from homework_2.vector import Vector
from homework_4.exceptions import CommandException


@dataclass
class CheckVelocityCommand(Command):
    movable: Movable

    def execute(self) -> None:
        if self.movable.get_velocity() == Vector(0, 0):
            raise CommandException()
