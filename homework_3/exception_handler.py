from homework_2.command import Command


class ExceptionHandler:
    _handlers: dict[type[Command], dict[type[Exception], type[Command]]]

    def __init__(self, queue):
        self._handlers = {}
        self.queue = queue

    def add_exception_handler(self, command: type[Command], exception: type[Exception], handler: type[Command]):
        self._handlers[command] = {exception: handler}

    def handle(self, command: Command, exception: type[Exception]) -> Command:
        try:
            return self._handlers[type(command)][exception](command=command, exception=exception, queue=self.queue)
        except KeyError:
            raise exception
