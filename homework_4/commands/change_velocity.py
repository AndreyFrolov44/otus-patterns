from dataclasses import dataclass
from homework_2.command import Command
from homework_2.vector import Vector
from homework_4.space_objects.movable_rotatable import MovableRotatableObject


@dataclass
class ChangeVelocityCommand(Command):
    obj: MovableRotatableObject

    def execute(self) -> None:
        velocity = self.obj.get_velocity()
        self.obj.set_velocity(Vector(velocity.x // 2, velocity.y // 2))
