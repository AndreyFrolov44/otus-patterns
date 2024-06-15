from typing import TYPE_CHECKING
from homework_2.command import Command

if TYPE_CHECKING:
    from homework_5.ioc import Scopes


class RegisterDependencyCommand(Command):
    def __init__(self, scopes: "Scopes", key, factory):
        self.scopes = scopes
        self.key = key
        self.factory = factory

    def execute(self):
        self.scopes.register(self.key, self.factory)


class CreateScopeCommand(Command):
    def __init__(self, scopes: "Scopes", scope_id: str):
        self.scopes = scopes
        self.scope_id = scope_id

    def execute(self):
        self.scopes.create_scope(self.scope_id)


class SetScopeCommand(Command):
    def __init__(self, scopes: "Scopes", scope_id: str):
        self.scopes = scopes
        self.scope_id = scope_id

    def execute(self):
        self.scopes.set_current_scope(self.scope_id)
