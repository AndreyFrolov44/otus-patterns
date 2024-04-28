from dataclasses import dataclass

from homework_2.vector import Vector


class Movable:
    def get_position(self) -> Vector:
        raise NotImplementedError()

    def set_position(self, position: Vector) -> None:
        raise NotImplementedError()

    def get_velocity(self) -> Vector:
        raise NotImplementedError()


@dataclass
class Move:
    _movable: Movable

    def execute(self) -> None:
        self._movable.set_position(self._movable.get_position() + self._movable.get_velocity())


@dataclass
class MovableObject(Movable):
    position: Vector
    velocity: Vector

    def get_position(self) -> Vector:
        return self.position

    def get_velocity(self) -> Vector:
        return self.velocity

    def set_position(self, position: Vector) -> None:
        self.position = position
