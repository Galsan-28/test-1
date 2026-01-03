from abc import ABC, abstractmethod
from enum import Enum


# Типы запросов
class RequestType(Enum):
    TYPE_A = "TYPE_A"
    TYPE_B = "TYPE_B"
    TYPE_C = "TYPE_C"
    TYPE_D = "TYPE_D"


# Класс запроса
class Request:
    def __init__(self, request_type: RequestType, content: str):
        self.type = request_type
        self.content = content


# Интерфейс обработчика
class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


# Конкретные обработчики
class ConcreteHandlerA(Handler):
    def handle(self, request: Request):
        if request.type == RequestType.TYPE_A:
            print(f"HandlerA обрабатывает запрос: {request.content}")
            return True
        else:
            print(f"HandlerA не может обработать {request.type}, передаю дальше")
            return super().handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request: Request):
        if request.type == RequestType.TYPE_B:
            print(f"HandlerB обрабатывает запрос: {request.content}")
            return True
        else:
            print(f"HandlerB не может обработать {request.type}, передаю дальше")
            return super().handle(request)


class ConcreteHandlerC(Handler):
    def handle(self, request: Request):
        if request.type == RequestType.TYPE_C:
            print(f"HandlerC обрабатывает запрос: {request.content}")
            return True
        else:
            print(f"HandlerC не может обработать {request.type}, передаю дальше")
            return super().handle(request)


class DefaultHandler(Handler):
    def handle(self, request: Request):
        print(f"DefaultHandler: Никто не смог обработать запрос типа {request.type}")
        return False


# Пример использования
def demonstrate_chain_of_responsibility():
    print("\n=== Chain of Responsibility Pattern ===")

    # Создаем цепочку
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConcreteHandlerC()
    default_handler = DefaultHandler()

    handler_a.set_next(handler_b).set_next(handler_c).set_next(default_handler)

    # Тестируем цепочку
    requests = [
        Request(RequestType.TYPE_A, "Запрос типа A"),
        Request(RequestType.TYPE_B, "Запрос типа B"),
        Request(RequestType.TYPE_C, "Запрос типа C"),
        Request(RequestType.TYPE_D, "Неизвестный запрос")
    ]

    for request in requests:
        print(f"\nОбработка: {request.type.value} - {request.content}")
        handler_a.handle(request)