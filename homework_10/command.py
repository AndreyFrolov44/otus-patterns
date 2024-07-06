from queue import Queue
from homework_2.command import Command


class MoveToCommand(Command):
    def __init__(self, queue: Queue):
        self.queue = queue

    def execute(self):
        return None


class RunCommand(Command):
    def execute(self):
        return None
