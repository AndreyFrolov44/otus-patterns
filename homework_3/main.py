from collections import deque

from homework_2.command import Command
from homework_3.exception_handler import ExceptionHandler


def do_commands(queue: deque[Command], exception_handler: ExceptionHandler):
    while queue:
        command = queue.popleft()

        try:
            command.execute()
        except Exception as e:
            exception_handler.handle(command, type(e)).execute()
