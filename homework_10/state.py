from abc import abstractmethod
from queue import Queue
from typing import TYPE_CHECKING

from homework_10.command import MoveToCommand, RunCommand
from homework_7.hard_stop import HardStop

if TYPE_CHECKING:
    from homework_10.consumer import Consumer
    from homework_2.command import Command


class State:
    def __init__(self, consumer: "Consumer") -> None:
        self.consumer = consumer

    @abstractmethod
    def handle(self, command: "Command"):
        """Возвращает ссылку на следующее состояние"""

    @abstractmethod
    def do_command(self, command: "Command") -> None:
        """Выполняет команду"""


class NormalState(State):
    def handle(self, command: "Command") -> State | None:
        if isinstance(command, HardStop):
            return None
        if isinstance(command, MoveToCommand):
            return MoveToState(self.consumer, command.queue)
        return self

    def do_command(self, command: "Command") -> None:
        command.execute()


class MoveToState(State):
    def __init__(self, consumer: "Consumer", queue: Queue) -> None:
        super().__init__(consumer)
        self.queue = queue

    def handle(self, command: "Command") -> State | None:
        if isinstance(command, HardStop):
            return None
        if isinstance(command, RunCommand):
            return NormalState(self.consumer)
        return self

    def do_command(self, command: "Command") -> None:
        self.queue.put(command)
