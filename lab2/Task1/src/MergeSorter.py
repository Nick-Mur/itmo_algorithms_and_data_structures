# Lab2/Task1/src/MergeSorter.py

"""Модуль с реализацией сортировки слиянием."""

class MergeSorter:
    """
    Класс для сортировки массива методом слияния.
    """

    @staticmethod
    def merge(array, left, middle, right):
        """
        Сливает два отсортированных подмассива array[left:middle+1] и array[middle+1:right+1].

        :param array: Исходный массив
        :param left: Начальный индекс левого подмассива
        :param middle: Конечный индекс левого подмассива
        :param right: Конечный индекс правого подмассива
        """
        if left < 0 or right >= len(array) or left > right:
            raise ValueError("Некорректные индексы для слияния.")

        left_subarray = array[left:middle + 1] + [float('inf')]
        right_subarray = array[middle + 1:right + 1] + [float('inf')]

        i = j = 0
        for k in range(left, right + 1):
            if left_subarray[i] <= right_subarray[j]:
                array[k] = left_subarray[i]
                i += 1
            else:
                array[k] = right_subarray[j]
                j += 1

    @staticmethod
    def merge_sort(array, left, right):
        """
        Рекурсивная сортировка слиянием.

        :param array: исходный массив
        :param left: начальный индекс
        :param right: конечный индекс
        """
        if left < 0 or right >= len(array):
            raise ValueError("Некорректные индексы для сортировки.")

        if left >= right:
            return

        middle = (left + right) // 2
        MergeSorter.merge_sort(array, left, middle)
        MergeSorter.merge_sort(array, middle + 1, right)
        MergeSorter.merge(array, left, middle, right)
