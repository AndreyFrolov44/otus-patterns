from homework_2.command import Command
import logging

logger = logging.getLogger(__name__)


class Log(Command):
    def __init__(self, *, command: Command, exception: Exception, **kwargs):
        self.command = command
        self.exception = exception

    def execute(self) -> None:
        logger.warning(f"Unexpected Error. Exception: {self.exception}, command: {self.command.__class__.__name__}")
