from homework_2.command import Command


class Retry(Command):
    def __init__(self, *, command: Command, **kwargs):
        self.command = command

    def execute(self):
        self.command.execute()


class DoubleRetry(Command):
    def __init__(self, *, command: Command, **kwargs):
        self.command = command

    def execute(self):
        self.command.execute()
