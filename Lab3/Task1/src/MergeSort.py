# lab1/src/algorithms/merge_sort.py

"""
Модуль с реализацией алгоритма Merge Sort.
"""

from typing import List


class MergeSort:
    """
    Класс, реализующий алгоритм Merge Sort.
    """

    def sort(self, arr: List[int]) -> List[int]:
        """
        Выполнение сортировки Merge Sort.

        :param arr: Список целых чисел для сортировки.
        :return: Отсортированный список целых чисел.
        """
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self._merge(left, right)

    @staticmethod
    def _merge(left: List[int], right: List[int]) -> List[int]:
        """
        Слияние двух отсортированных списков.

        :param left: Отсортированный левый список.
        :param right: Отсортированный правый список.
        :return: Объединенный отсортированный список.
        """
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # Добавляем оставшиеся элементы
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
