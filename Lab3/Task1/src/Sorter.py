from Lab3.Task1.src.QuickSort import QuickSort
from Lab3.Task1.src.MergeSort import MergeSort


class Sorter:
    """
    Класс, объединяющий различные алгоритмы сортировки.
    """

    def __init__(self):
        self.quick_sort = QuickSort()
        self.merge_sort = MergeSort()

    def perform_sorting(self, arr: list) -> dict:
        """
        Выполнение различных сортировок и возврат результатов.

        :param arr: Исходный список целых чисел.
        :return: Словарь с отсортированными списками.
        """
        results = {}

        # Простая QuickSort
        arr_quick = arr.copy()
        self.quick_sort.simple_sort(arr_quick)
        results['simple_quick_sort'] = arr_quick

        # Randomized QuickSort
        arr_randomized = arr.copy()
        self.quick_sort.randomized_sort(arr_randomized)
        results['randomized_quick_sort'] = arr_randomized

        # Randomized QuickSort с Partition3
        arr_randomized_p3 = arr.copy()
        self.quick_sort.randomized_sort_partition3(arr_randomized_p3)
        results['randomized_quick_sort_partition3'] = arr_randomized_p3

        # Merge Sort
        arr_merge_sorted = self.merge_sort.sort(arr.copy())
        results['merge_sort'] = arr_merge_sorted

        return results
