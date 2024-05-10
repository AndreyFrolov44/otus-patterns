import threading
from typing import Callable

from homework_5.commands import CreateScopeCommand, RegisterDependencyCommand, SetScopeCommand


class ScopeLocal(threading.local):
    def __init__(self):
        super().__init__()
        self.value = "default"


class Scopes:
    _current_scope = ScopeLocal()
    _scopes: dict[str, dict[str, Callable]] = {_current_scope.value: {}}

    def resolve(self, key: str, *args):
        if key in self._scopes[self._current_scope.value]:
            return self._scopes[self._current_scope.value][key](*args)
        raise KeyError(f"Unknown dependency '{key}'")

    def create_scope(self, key: str):
        if key in self._scopes:
            raise Exception(f"Scope '{key}' already exists")
        self._scopes[key] = {}

    def get_current_scope(self):
        return self._current_scope.value

    def set_current_scope(self, key: str):
        if key not in self._scopes:
            raise Exception(f"Scope '{key}' is not exists")
        self._current_scope.value = key

    def register(self, key, factory):
        self._scopes[self._current_scope.value][key] = factory


class IoC:
    _scopes = Scopes()

    @classmethod
    def resolve(cls, key: str, *args):
        if key == "IoC.Register":
            if len(args) != 2:
                raise Exception(f"You have to pass 2 arguments, and you passed {len(args)}")
            return RegisterDependencyCommand(cls._scopes, args[0], args[1])
        elif key == "Scopes.New":
            if len(args) != 1:
                raise Exception(f"You have to pass 1 arguments, and you passed {len(args)}")
            return CreateScopeCommand(cls._scopes, args[0])
        elif key == "Scopes.Current":
            if len(args) != 1:
                raise Exception(f"You have to pass 1 arguments, and you passed {len(args)}")
            return SetScopeCommand(cls._scopes, args[0])
        else:
            return cls._resolve_dependency(key, *args)

    @classmethod
    def _resolve_dependency(cls, key: str, *args):
        return cls._scopes.resolve(key, *args)
