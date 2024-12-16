# Lab2/Task4/src/BinarySearcher.py

"""Модуль для бинарного поиска элемента."""

class BinarySearcher:
    """
    Класс для выполнения бинарного поиска в отсортированном массиве.
    """

    @staticmethod
    def binary_search(array, target):
        """
        Выполняет бинарный поиск целевого элемента в отсортированном массиве.

        :param array: Отсортированный список целых чисел.
        :param target: Целевое число для поиска.
        :return: Индекс элемента (0-based) или -1, если не найден.
        """
        if not isinstance(array, list):
            raise TypeError("Ожидается массив (list).")

        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def multi_search(array, targets):
        """
        Выполняет бинарный поиск для нескольких целевых чисел.

        :param array: Отсортированный список целых чисел.
        :param targets: Список целевых чисел для поиска.
        :return: Список индексов или -1 для каждого целевого числа.
        """
        return [BinarySearcher.binary_search(array, target) for target in targets]
