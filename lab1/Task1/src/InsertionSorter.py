# Lab1/Task1/src/InsertionSorter.py

"""Модуль для сортировки массива методом вставки."""

class InsertionSorter:
    """
    Класс для сортировки массива методом вставки по возрастанию.
    """

    @staticmethod
    def insertion_sort(arr):
        """
        Сортирует массив методом вставки по возрастанию.

        :param arr: Список целых чисел.
        :return: Отсортированный список.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
