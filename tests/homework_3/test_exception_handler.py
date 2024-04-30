from collections import deque
import logging

import pytest
from homework_2.move import MovableObject, Move
from homework_2.vector import Vector
from homework_3.commands.add_queue import AddDoubleRetryToQueue, AddLogToQueue, AddRetryToQueue
from homework_3.commands.log import Log
from homework_3.commands.retry import DoubleRetry, Retry
from homework_3.exception_handler import ExceptionHandler
from homework_3.main import do_commands


def test_log_exception_handler(mocker, caplog):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    move = Move(movable_object)

    queue = deque([move])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=Log)

    with caplog.at_level(logging.WARNING):
        do_commands(queue, exception_handler)

    assert "Unexpected Error. Exception: <class 'TypeError'>, command: Move" in caplog.text


def test_add_log_to_queue_exception_handler(mocker, caplog):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    move = Move(movable_object)

    queue = deque([move])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=AddLogToQueue)

    with caplog.at_level(logging.WARNING):
        do_commands(queue, exception_handler)

    assert "Unexpected Error. Exception: <class 'TypeError'>, command: Move" in caplog.text


def test_retry_exception_handler(mocker):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocked_movable_object = mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    command = Move(movable_object)

    queue = deque([command])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=Retry)

    pytest.raises(TypeError, do_commands, queue, exception_handler)

    assert mocked_movable_object.call_count == 2


def test_add_retry_to_queue_exception_handler(mocker):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocked_movable_object = mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    command = Move(movable_object)

    queue = deque([command])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=AddRetryToQueue)

    pytest.raises(TypeError, do_commands, queue, exception_handler)

    assert mocked_movable_object.call_count == 2


def test_retry_and_log_exception_handler(mocker, caplog):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocked_movable_object = mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    command = Move(movable_object)

    queue = deque([command])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=AddRetryToQueue)
    exception_handler.add_exception_handler(command=Retry, exception=TypeError, handler=AddLogToQueue)

    with caplog.at_level(logging.WARNING):
        do_commands(queue, exception_handler)

    assert mocked_movable_object.call_count == 2


def test_double_retry_and_log_exception_handler(mocker, caplog):
    movable_object = MovableObject(position=Vector(12, 5), velocity=Vector(-7, 3))
    mocked_movable_object = mocker.patch.object(movable_object, "get_position", side_effect=TypeError)
    command = Move(movable_object)

    queue = deque([command])

    exception_handler = ExceptionHandler(queue)
    exception_handler.add_exception_handler(command=Move, exception=TypeError, handler=AddRetryToQueue)
    exception_handler.add_exception_handler(command=Retry, exception=TypeError, handler=AddDoubleRetryToQueue)
    exception_handler.add_exception_handler(command=DoubleRetry, exception=TypeError, handler=AddLogToQueue)

    with caplog.at_level(logging.WARNING):
        do_commands(queue, exception_handler)

    assert mocked_movable_object.call_count == 3
