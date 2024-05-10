import pytest
from homework_2.vector import Vector
from homework_4.commands.check_burn_fuel_move import CheckBurnFuelMoveCommand
from homework_4.exceptions import CommandException
from homework_4.space_objects.movable_refueled import MovableRefueledObject


def test_check_burn_fuel_move_success():
    movable_refueled_object = MovableRefueledObject(
        fuel=1,
        fuel_velocity=1,
        position=Vector(0, 0),
        velocity=Vector(1, 1),
    )
    cmd = CheckBurnFuelMoveCommand(movable_refueled_object)

    cmd.execute()

    assert movable_refueled_object.get_fuel() == 0


@pytest.mark.parametrize("fuel", [-1, 0, 1])
def test_check_burn_fuel_move_exception(fuel: int):
    movable_refueled_object = MovableRefueledObject(
        fuel=fuel,
        fuel_velocity=2,
        position=Vector(0, 0),
        velocity=Vector(1, 1),
    )
    cmd = CheckBurnFuelMoveCommand(movable_refueled_object)

    pytest.raises(CommandException, cmd.execute)
