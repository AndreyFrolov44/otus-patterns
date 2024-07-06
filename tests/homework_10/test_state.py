from queue import Queue
from unittest.mock import Mock
from homework_10.command import MoveToCommand, RunCommand
from homework_10.consumer import Consumer
from homework_10.state import MoveToState
from homework_2.command import Command
from homework_7.hard_stop import HardStop


def test_state_hard_stop():
    queue = Queue()
    command = Mock(spec=Command)
    queue.put(command)

    consumer = Consumer(queue, Mock())
    queue.put(HardStop(consumer))
    consumer()

    assert command.execute.called


def test_state_move_to():
    queue = Queue()
    new_queue = Queue()
    queue.put(MoveToCommand(new_queue))
    command = Mock(spec=Command)
    queue.put(command)

    consumer = Consumer(queue, Mock())
    queue.put(HardStop(consumer))
    consumer()

    assert not command.execute.called
    assert not new_queue.empty()
    assert queue.empty()


def test_state_run_command():
    queue = Queue()
    new_queue = Queue()
    queue.put(RunCommand())
    command = Mock(spec=Command)
    queue.put(command)

    consumer = Consumer(queue, Mock())
    consumer.state = MoveToState(consumer, new_queue)
    queue.put(HardStop(consumer))
    consumer()

    assert command.execute.called
    assert new_queue.empty()
    assert queue.empty()
