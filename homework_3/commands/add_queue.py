from collections import deque

from homework_2.command import Command
from homework_3.commands.log import Log
from homework_3.commands.retry import DoubleRetry, Retry


class AddLogToQueue(Command):
    def __init__(self, *, command: Command, exception: Exception, queue: deque[Command], **kwargs):
        self.command = command
        self.exception = exception
        self.queue = queue

    def execute(self):
        self.queue.append(Log(command=self.command, exception=self.exception))


class AddRetryToQueue(Command):
    def __init__(self, *, command: Command, queue: deque[Command], **kwargs):
        self.command = command
        self.queue = queue

    def execute(self):
        self.queue.append(Retry(command=self.command))


class AddDoubleRetryToQueue(Command):
    def __init__(self, *, command: Command, queue: deque[Command], **kwargs):
        self.command = command
        self.queue = queue

    def execute(self):
        self.queue.append(DoubleRetry(command=self.command))
