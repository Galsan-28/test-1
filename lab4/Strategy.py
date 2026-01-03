from abc import ABC, abstractmethod
from typing import List


# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


# Конкретные стратегии
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Сортировка пузырьком")
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Быстрая сортировка")

        def _quick_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return _quick_sort(left) + middle + _quick_sort(right)

        return _quick_sort(data.copy())


class InsertionSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        print("Сортировка вставками")
        arr = data.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


# Контекст
class Sorter:
    def __init__(self, strategy: SortingStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        if not self._strategy:
            raise ValueError("Стратегия не установлена")
        return self._strategy.sort(data)


# Пример использования
def demonstrate_strategy():
    print("=== Strategy Pattern ===")
    data = [64, 34, 25, 12, 22, 11, 90]
    sorter = Sorter()

    # Используем разные стратегии
    strategies = {
        "Bubble": BubbleSortStrategy(),
        "Quick": QuickSortStrategy(),
        "Insertion": InsertionSortStrategy()
    }

    for name, strategy in strategies.items():
        sorter.set_strategy(strategy)
        result = sorter.sort_data(data)
        print(f"{name} sort result: {result}\n")