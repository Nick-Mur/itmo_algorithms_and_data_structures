"""
Модуль с реализациями алгоритма QuickSort.
"""

import random
from typing import List, Tuple


class QuickSort:
    """
    Класс, реализующий различные варианты алгоритма QuickSort.
    """

    def simple_sort(self, arr: List[int]) -> None:
        """
        Простая реализация алгоритма QuickSort.

        :param arr: Список целых чисел для сортировки.
        """
        self._simple_quick_sort(arr, 0, len(arr) - 1)

    def randomized_sort(self, arr: List[int]) -> None:
        """
        Реализация Randomized QuickSort.

        :param arr: Список целых чисел для сортировки.
        """
        self._randomized_quick_sort(arr, 0, len(arr) - 1)

    def randomized_sort_partition3(self, arr: List[int]) -> None:
        """
        Реализация Randomized QuickSort с трехчастным разделением (Partition3).

        :param arr: Список целых чисел для сортировки.
        """
        self._randomized_quick_sort_partition3(arr, 0, len(arr) - 1)

    def _simple_quick_sort(self, arr: List[int], low: int, high: int) -> None:
        """
        Рекурсивная простая QuickSort.

        :param arr: Список целых чисел.
        :param low: Начальный индекс подмассива.
        :param high: Конечный индекс подмассива.
        """
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._simple_quick_sort(arr, low, pivot_index - 1)
            self._simple_quick_sort(arr, pivot_index + 1, high)

    def _randomized_quick_sort(self, arr: List[int], low: int, high: int) -> None:
        """
        Рекурсивная Randomized QuickSort.

        :param arr: Список целых чисел.
        :param low: Начальный индекс подмассива.
        :param high: Конечный индекс подмассива.
        """
        if low < high:
            pivot_index = self._randomized_partition(arr, low, high)
            self._randomized_quick_sort(arr, low, pivot_index - 1)
            self._randomized_quick_sort(arr, pivot_index + 1, high)

    def _randomized_quick_sort_partition3(self, arr: List[int], low: int, high: int) -> None:
        """
        Рекурсивная Randomized QuickSort с трехчастным разделением.

        :param arr: Список целых чисел.
        :param low: Начальный индекс подмассива.
        :param high: Конечный индекс подмассива.
        """
        if low < high:
            m1, m2 = self._partition3(arr, low, high)
            self._randomized_quick_sort_partition3(arr, low, m1 - 1)
            self._randomized_quick_sort_partition3(arr, m2 + 1, high)

    @staticmethod
    def _partition(arr: List[int], low: int, high: int) -> int:
        """
        Обычная процедура разделения массива для QuickSort.

        :param arr: Список целых чисел.
        :param low: Начальный индекс.
        :param high: Конечный индекс.
        :return: Индекс опорного элемента.
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # Помещаем опорный элемент на правильную позицию
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _randomized_partition(self, arr: List[int], low: int, high: int) -> int:
        """
        Рандомизированная процедура разделения.

        :param arr: Список целых чисел.
        :param low: Начальный индекс.
        :param high: Конечный индекс.
        :return: Индекс опорного элемента.
        """
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        return self._partition(arr, low, high)

    @staticmethod
    def _partition3(arr: List[int], low: int, high: int) -> Tuple[int, int]:
        """
        Трехчастная процедура разделения массива для обработки дубликатов.

        :param arr: Список целых чисел.
        :param low: Начальный индекс.
        :param high: Конечный индекс.
        :return: Кортеж из двух индексов m1 и m2.
        """
        pivot = arr[high]
        m1 = low
        m2 = high
        i = low
        while i <= m2:
            if arr[i] < pivot:
                arr[m1], arr[i] = arr[i], arr[m1]
                m1 += 1
                i += 1
            elif arr[i] > pivot:
                arr[m2], arr[i] = arr[i], arr[m2]
                m2 -= 1
            else:
                i += 1
        return m1, m2
