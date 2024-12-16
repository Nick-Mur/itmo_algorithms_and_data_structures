# Lab1/Task2/src/InsertionSorterWithIndices.py

"""Модуль для сортировки вставками с отслеживанием индексов элементов."""

class InsertionSorterWithIndices:
    """
    Класс для сортировки вставками с отслеживанием конечных позиций элементов.
    """

    @staticmethod
    def insertion_sort_with_indices(arr):
        """
        Сортировка вставками с отслеживанием индексов.

        Возвращает кортеж (список конечных индексов, отсортированный список).

        :param arr: Список целых чисел.
        :return: (список индексов, отсортированный список)
        """
        index_result = [1]
        for i in range(1,len(arr)):
            # Простой, но не очень корректный вариант из исходного кода (оптимизируем)
            key = arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1]=key
            # Индекс в конечном итоге j+1
            # Так как индексация с 1, добавляем +1
            index_result.append(j+2)
        return index_result, arr
