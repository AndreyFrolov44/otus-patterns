import pytest
from homework_2.angle import Angle
from homework_2.vector import Vector
from homework_4.commands.rotate_change_velocity import RotateChangeVelocityCommand
from homework_4.exceptions import CommandException
from homework_4.space_objects.movable_rotatable import MovableRotatableObject


def test_rotate_change_velocity_success():
    rotate_change_velocity_object = MovableRotatableObject(
        angle=Angle(1),
        angular_velocity=Angle(1),
        position=Vector(0, 0),
        velocity=Vector(2, 5),
    )
    cmd = RotateChangeVelocityCommand(rotate_change_velocity_object)

    cmd.execute()

    assert rotate_change_velocity_object.get_velocity() == Vector(1, 2)


def test_rotate_change_velocity__exception():
    rotate_change_velocity_object = MovableRotatableObject(
        angle=Angle(1),
        angular_velocity=Angle(1),
        position=Vector(0, 0),
        velocity=Vector(0, 0),
    )
    cmd = RotateChangeVelocityCommand(rotate_change_velocity_object)

    pytest.raises(CommandException, cmd.execute)
