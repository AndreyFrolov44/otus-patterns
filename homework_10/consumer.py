from typing import TYPE_CHECKING
from queue import Empty, Queue

from homework_10.state import NormalState, State
from homework_3.exception_handler import ExceptionHandler


if TYPE_CHECKING:
    from homework_2.command import Command


class Consumer:
    def __init__(self, queue: Queue, exception_handler: ExceptionHandler) -> None:
        self.state: State | None = NormalState(self)
        self.queue = queue
        self.exception_handler = exception_handler
        self._stop = False

    def __call__(self) -> None:
        while not self._stop:
            try:
                command: "Command" = self.queue.get()
            except Empty:
                pass
            else:
                self._do_command(command)
                self.queue.task_done()

    def _do_command(self, command: "Command") -> None:
        try:
            if self.state is None:
                self.stop()
                return
            self.state = self.state.handle(command)
            if self.state is not None:
                self.state.do_command(command)
            else:
                command.execute()
        except Exception as exc:
            self.exception_handler.handle(command, type(exc)).execute()

    def stop(self):
        self._stop = True
