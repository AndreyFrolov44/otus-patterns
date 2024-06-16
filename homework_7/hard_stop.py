from homework_2.command import Command
from homework_7.consumer import Consumer


class HardStop(Command):
    def __init__(self, consumer: Consumer):
        self.consumer = consumer

    def execute(self):
        self.consumer.stop()
