from queue import Empty
from homework_2.command import Command
from homework_7.consumer import Consumer


class SoftStop(Command):
    def __init__(self, consumer: Consumer):
        self.consumer = consumer

    def execute(self):
        self.consumer.behavior = self._behavior

    def _behavior(self):
        try:
            command: Command = self.consumer.queue.get_nowait()
        except Empty:
            self.consumer.stop()
        else:
            self.consumer._do_command(command)
            self.consumer.queue.task_done()
