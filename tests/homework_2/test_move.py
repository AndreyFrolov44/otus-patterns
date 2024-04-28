import pytest
from homework_2.move import MovableObject, Move
from homework_2.vector import Vector


def test_move():
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    move = Move(movable_object)

    move.execute()

    assert movable_object.position == Vector(5, 8)


def test_get_position_exception(mocker):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocker.patch.object(movable_object, "get_position", side_effect=RuntimeError)
    move = Move(movable_object)

    with pytest.raises(RuntimeError):
        move.execute()


def test_get_velocity_exception(mocker):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocker.patch.object(movable_object, "get_velocity", side_effect=RuntimeError)
    move = Move(movable_object)

    with pytest.raises(RuntimeError):
        move.execute()


def test_set_position_exception(mocker):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocker.patch.object(movable_object, "set_position", side_effect=RuntimeError)
    move = Move(movable_object)

    with pytest.raises(RuntimeError):
        move.execute()
