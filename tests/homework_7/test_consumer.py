from queue import Queue
from threading import Thread
from unittest.mock import Mock

from homework_2.command import Command
from homework_7.consumer import Consumer
from homework_7.hard_stop import HardStop
from homework_7.soft_stop import SoftStop


def test_consumer_hard_stop():
    queue = Queue()
    command = Mock(spec=Command)

    producer_thread = Thread(target=lambda: queue.put(command))
    producer_thread.start()

    consumer = Consumer(queue, Mock())
    consumer_thread = Thread(target=consumer)
    consumer_thread.start()

    producer_thread.join()
    queue.put(HardStop(consumer))
    consumer_thread.join()

    assert command.execute.called


def test_consumer_soft_stop():
    queue = Queue()
    consumer = Consumer(queue, Mock())
    commands = [
        Mock(spec=Command),
        Mock(spec=Command),
        Mock(spec=Command),
        SoftStop(consumer),
        Mock(spec=Command),
        Mock(spec=Command),
    ]
    for command in commands:
        queue.put(command)

    consumer_thread = Thread(target=consumer)
    consumer_thread.start()

    consumer_thread.join()

    assert all([command.execute.called for command in commands if type(command) is not SoftStop])
