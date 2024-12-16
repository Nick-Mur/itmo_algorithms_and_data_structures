# Lab1/Task3/src/InsertionSorterDescending.py

"""Модуль для сортировки массива методом вставки по убыванию."""

class InsertionSorterDescending:
    """
    Класс для сортировки массива методом вставки по убыванию.
    """

    @staticmethod
    def insertion_sort_descending(arr):
        for i in range(1,len(arr)):
            key=arr[i]
            j=i-1
            while j>=0 and arr[j]<key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
        return arr
