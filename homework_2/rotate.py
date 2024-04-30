from dataclasses import dataclass

from homework_2.angle import Angle
from homework_2.command import Command


class Rotatable:
    def get_angle(self) -> Angle:
        raise NotImplementedError()

    def set_angle(self, angle: Angle) -> None:
        raise NotImplementedError()

    def get_angular_velocity(self) -> Angle:
        raise NotImplementedError()


@dataclass
class Rotate(Command):
    _rotatable: Rotatable

    def execute(self) -> None:
        self._rotatable.set_angle(self._rotatable.get_angle() + self._rotatable.get_angular_velocity())


@dataclass
class RotatableObject(Rotatable):
    angle: Angle
    angular_velocity: Angle

    def get_angle(self) -> Angle:
        return self.angle

    def set_angle(self, angle: Angle) -> None:
        self.angle = angle

    def get_angular_velocity(self) -> Angle:
        return self.angular_velocity
