# Lab1/Task5/src/SelectionSorter.py

"""Модуль для сортировки выбором."""

class SelectionSorter:
    """
    Класс для сортировки массива методом выбора.
    """

    @staticmethod
    def selection_sort(arr):
        for i in range(len(arr)):
            min_idx=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_idx]:
                    min_idx=j
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
        return arr
