from dataclasses import dataclass
from homework_2.angle import Angle
from homework_2.move import MovableObject
from homework_2.rotate import RotatableObject
from homework_2.vector import Vector


@dataclass
class MovableRotatableObject(MovableObject, RotatableObject):
    angle: Angle
    angular_velocity: Angle

    position: Vector
    velocity: Vector
