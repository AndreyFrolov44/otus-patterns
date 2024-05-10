from homework_2.move import MovableObject
from homework_2.vector import Vector
from homework_4.commands.change_velocity import ChangeVelocityCommand


def test_change_velocity():
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(5, 3))
    cmd = ChangeVelocityCommand(movable_object)

    cmd.execute()

    assert movable_object.get_velocity() == Vector(2, 1)
