from queue import Empty, Queue

from homework_2.command import Command
from homework_3.exception_handler import ExceptionHandler


class Consumer:
    def __init__(self, queue: Queue, exception_handler: ExceptionHandler) -> None:
        self.queue = queue
        self.exception_handler = exception_handler
        self._stop = False
        self.behavior = self._behavior

    def _behavior(self) -> None:
        try:
            command: Command = self.queue.get()
        except Empty:
            pass
        else:
            self._do_command(command)
            self.queue.task_done()

    def __call__(self):
        while not self._stop:
            self.behavior()

    def _do_command(self, command: Command) -> None:
        try:
            command.execute()
        except Exception as exc:
            self.exception_handler.handle(command, type(exc)).execute()

    def stop(self):
        self._stop = True
