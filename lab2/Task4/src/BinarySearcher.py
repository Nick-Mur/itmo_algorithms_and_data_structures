# Lab2/Task4/src/BinarySearcher.py

"""Модуль для бинарного поиска элемента."""

class BinarySearcher:
    """
    Класс для выполнения бинарного поиска в отсортированном массиве.
    """

    @staticmethod
    def binary_search(array, target):
        if not isinstance(array, list):
            raise TypeError("Ожидается массив (list).")

        left=0
        right=len(array)-1

        while left<=right:
            mid=(left+right)//2
            if array[mid]==target:
                return mid
            elif array[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
