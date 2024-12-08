# Lab5/Task7/src/HeapSorter.py

"""Модуль для пирамидальной сортировки массива."""


class HeapSorter:
    """
    Класс для выполнения пирамидальной (heap) сортировки массива.
    """

    def heapify(self, arr, n, i):
        """
        Преобразование поддерева с корнем в индексе i в max-heap.

        :param arr: Массив.
        :param n: Размер участка массива.
        :param i: Индекс корня поддерева.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapsort(self, arr):
        """
        Пирамидальная сортировка массива arr.

        :param arr: Массив для сортировки.
        """
        n = len(arr)

        # Построение max-heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # Извлечение элементов из кучи
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
