import pytest
from homework_4.commands.burn_fuel import BurnFuelCommand
from homework_4.space_objects.refueled import RefueledObject


@pytest.mark.parametrize(
    ("start_fuel", "fuel_velocity", "expected_fuel"),
    [
        (0, 5, 0),
        (5, 5, 0),
        (5, 1, 4),
    ],
)
def test_burn_fuel(start_fuel: int, fuel_velocity: int, expected_fuel: int):
    refueled_object = RefueledObject(start_fuel, fuel_velocity)
    cmd = BurnFuelCommand(refueled_object)

    cmd.execute()

    assert refueled_object.fuel == expected_fuel
