import pytest
from homework_2.move import MovableObject
from homework_2.vector import Vector
from homework_5.ioc import IoC
import threading


def test_ioc_create():
    IoC.resolve("IoC.Register", "MovableObject", lambda position, velocity: MovableObject(position, velocity)).execute()

    assert IoC.resolve("MovableObject", Vector(0, 0), Vector(1, 1)) == MovableObject(Vector(0, 0), Vector(1, 1))


def test_new_scope():
    IoC.resolve("Scopes.New", "game").execute()

    assert "game" in IoC._scopes._scopes


def test_set_current_scope_not_exists():
    with pytest.raises(Exception):
        IoC.resolve("Scopes.Current", "not exists").execute()


def test_set_scope_already_exists():
    IoC.resolve("Scopes.New", "test").execute()

    with pytest.raises(Exception):
        IoC.resolve("Scopes.New", "test").execute()


def test_unknown_dependency():
    with pytest.raises(Exception):
        IoC.resolve("unknown").execute()


@pytest.mark.parametrize(
    ("ioc_command", "args"),
    [
        ("IoC.Register", []),
        ("IoC.Register", [1]),
        ("IoC.Register", [1, 2, 3]),
        ("Scopes.New", []),
        ("Scopes.New", [1, 2]),
        ("Scopes.Current", []),
        ("Scopes.Current", [1, 2]),
    ],
)
def test_wrong_args(ioc_command, args):
    with pytest.raises(Exception):
        IoC.resolve("ioc_command", *args).execute()


def test_thread():
    IoC.resolve("Scopes.New", "thread1")
    IoC.resolve("Scopes.New", "thread2")

    def ioc_thread(scope):
        IoC.resolve("Scopes.Current", scope)

    threads = [
        threading.Thread(target=ioc_thread, args=("thread1")),
        threading.Thread(target=ioc_thread, args=("thread2")),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert IoC._scopes.get_current_scope() == "default"
