from dataclasses import dataclass
from homework_2.move import MovableObject
from homework_2.vector import Vector
from homework_4.space_objects.refueled import RefueledObject


@dataclass
class MovableRefueledObject(MovableObject, RefueledObject):
    fuel: int
    fuel_velocity: int

    position: Vector
    velocity: Vector
