from abc import ABC, abstractmethod
from typing import Any, List


# Интерфейс итератора
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> Any:
        pass


# Интерфейс коллекции
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


# Конкретный итератор для массива
class ArrayIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._collection)

    def next(self) -> Any:
        if not self.has_next():
            raise StopIteration()
        item = self._collection[self._position]
        self._position += 1
        return item

    def reset(self):
        self._position = 0


# Конкретный итератор для обратного обхода
class ReverseArrayIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._position = len(collection) - 1

    def has_next(self) -> bool:
        return self._position >= 0

    def next(self) -> Any:
        if not self.has_next():
            raise StopIteration()
        item = self._collection[self._position]
        self._position -= 1
        return item


# Коллекция
class NumberCollection(IterableCollection):
    def __init__(self):
        self._numbers = []

    def add_number(self, number: int):
        self._numbers.append(number)

    def create_iterator(self) -> Iterator:
        return ArrayIterator(self._numbers)

    def create_reverse_iterator(self) -> Iterator:
        return ReverseArrayIterator(self._numbers)


# Пример использования
def demonstrate_iterator():
    print("\n=== Iterator Pattern ===")

    collection = NumberCollection()
    for i in range(1, 6):
        collection.add_number(i * 10)

    # Прямой итератор
    print("Прямой обход:")
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next(), end=" ")
    print()

    # Обратный итератор
    print("Обратный обход:")
    reverse_iterator = collection.create_reverse_iterator()
    while reverse_iterator.has_next():
        print(reverse_iterator.next(), end=" ")
    print()