import inspect
from homework_2.command import Command
from homework_5.ioc import IoC


class UObject:
    def get_property(self, key: str):
        raise NotImplementedError()

    def set_property(self, key: str, value: object):
        raise NotImplementedError()


class AdapterFactoryCommand(Command):
    def __init__(self, interface, obj):
        self.interface = interface
        self.obj = obj

    def register_method(self, method):
        interface = self.interface
        if method.startswith("set"):

            def set_filed(self, value):
                IoC.resolve(f"{interface.__name__}:{method[4:]}.set", self.obj, value).execute()

            f = set_filed
        elif method.startswith("get"):

            def get_field(self):
                return IoC.resolve(f"{interface.__name__}:{method[4:]}.get", self.obj)

            f = get_field
        else:
            raise TypeError
        return f

    def execute(self):
        def __init__(self, obj):
            self.obj = obj

        class_methods = dict(__init__=__init__)

        for method, _ in inspect.getmembers(self.interface, predicate=inspect.isfunction):
            class_methods[method] = self.register_method(method)

        return type(f"{self.interface.__name__}Adapter", (self.interface,), class_methods)(self.obj)
