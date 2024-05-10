from unittest.mock import Mock

import pytest
from homework_2.command import Command, MacroCommand


def test_macro_command():
    commands = [Mock(Command) for _ in range(5)]
    cmd = MacroCommand(commands)

    cmd.execute()

    assert all(command.execute.called for command in commands)


def test_raise_exception_from_macro_command(mocker):
    commands = [Mock(Command) for _ in range(5)]
    mocker.patch.object(commands[3], "execute", side_effect=Exception())
    cmd = MacroCommand(commands)

    pytest.raises(Exception, cmd.execute)
