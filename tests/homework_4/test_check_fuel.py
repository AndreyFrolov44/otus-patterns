import pytest
from homework_4.commands.check_fuel import CheckFuelCommand
from homework_4.exceptions import CommandException
from homework_4.space_objects.refueled import RefueledObject


@pytest.mark.parametrize("start_fuel", [0, 1])
def test_check_fuel_exception(start_fuel: int):
    refueled_object = RefueledObject(start_fuel, 2)
    cmd = CheckFuelCommand(refueled_object)

    pytest.raises(CommandException, cmd.execute)


def test_check_fuel_success():
    refueled_object = RefueledObject(1, 1)
    cmd = CheckFuelCommand(refueled_object)

    cmd.execute()
