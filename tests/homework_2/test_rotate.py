import pytest
from homework_2.angle import Angle
from homework_2.rotate import RotatableObject, Rotate


def test_rotate():
    rotatable_object = RotatableObject(angle=Angle(120), angular_velocity=Angle(60))
    rotate = Rotate(rotatable_object)

    rotate.execute()

    assert rotatable_object.angle == Angle(180)


def test_get_angle_exception(mocker):
    rotatable_object = RotatableObject(angle=Angle(120), angular_velocity=Angle(60))
    mocker.patch.object(rotatable_object, "get_angle", side_effect=RuntimeError)
    rotate = Rotate(rotatable_object)

    with pytest.raises(RuntimeError):
        rotate.execute()


def test_get_angular_velocity_exception(mocker):
    rotatable_object = RotatableObject(angle=Angle(120), angular_velocity=Angle(60))
    mocker.patch.object(rotatable_object, "get_angular_velocity", side_effect=RuntimeError)
    rotate = Rotate(rotatable_object)

    with pytest.raises(RuntimeError):
        rotate.execute()


def test_set_angle_exception(mocker):
    rotatable_object = RotatableObject(angle=Angle(120), angular_velocity=Angle(60))
    mocker.patch.object(rotatable_object, "set_angle", side_effect=RuntimeError)
    rotate = Rotate(rotatable_object)

    with pytest.raises(RuntimeError):
        rotate.execute()
