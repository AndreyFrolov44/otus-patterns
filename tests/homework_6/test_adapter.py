from unittest.mock import Mock
from homework_5.ioc import IoC
from homework_6.adapter import AdapterFactoryCommand, UObject


class TestInterface:
    def get_field(self):
        raise NotImplementedError

    def set_field(self, value):
        raise NotImplementedError


def test_adapter_get_field(mocker):
    resolve = mocker.patch("homework_5.ioc.IoC.resolve")
    obj = Mock(UObject)

    adapter = AdapterFactoryCommand(TestInterface, obj).execute()
    adapter.get_field()

    resolve.assert_called_with("TestInterface:field.get", obj)


def test_adapter_set_field(mocker):
    resolve = mocker.patch("homework_5.ioc.IoC.resolve")
    obj = Mock(UObject)

    adapter = AdapterFactoryCommand(TestInterface, obj).execute()
    adapter.set_field(123)

    resolve.assert_called_with("TestInterface:field.set", obj, 123)


def test_adapter_ioc(mocker):
    IoC.resolve(
        "IoC.Register", "Adapter", lambda interface, obj: AdapterFactoryCommand(interface, obj).execute()
    ).execute()
    obj = Mock(UObject)

    adapter = IoC.resolve("Adapter", TestInterface, obj)
    resolve = mocker.patch("homework_5.ioc.IoC.resolve")
    adapter.set_field(123)

    resolve.assert_called_with("TestInterface:field.set", obj, 123)
