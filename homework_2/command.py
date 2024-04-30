from dataclasses import dataclass
from homework_4.exceptions import CommandException


class Command:
    def __init__(self, *args, **kwargs):
        return

    def execute(self):
        raise NotImplementedError()


@dataclass
class MacroCommand(Command):
    commands: list[Command]

    def execute(self) -> None:
        for command in self.commands:
            try:
                command.execute()
            except Exception as e:
                raise CommandException(e)
