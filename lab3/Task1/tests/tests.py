"""
Модуль с тестами для алгоритмов сортировки.
"""

import unittest
from lab3.Task1.src.MergeSort import MergeSort
from lab3.Task1.src.QuickSort import QuickSort


class TestSortingAlgorithms(unittest.TestCase):
    """
    Класс для тестирования алгоритмов сортировки.
    """

    def setUp(self):
        """
        Инициализация данных для тестов.
        """
        self.quick_sort = QuickSort()
        self.merge_sort = MergeSort()

        self.empty_list = []
        self.single_element_list = [1]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.reverse_sorted_list = [5, 4, 3, 2, 1]
        self.random_list = [3, 6, 2, 8, 1, 5]
        self.duplicate_list = [2, 3, 2, 3, 1, 1]
        self.all_same = [7, 7, 7, 7, 7]

    def test_should_simple_quick_sort_empty(self):
        """
        Тестирование simple_sort на пустом массиве.
        """
        arr = self.empty_list.copy()
        self.quick_sort.simple_sort(arr)
        self.assertEqual(arr, [])

    def test_should_simple_quick_sort_single(self):
        """
        Тестирование simple_sort на массиве с одним элементом.
        """
        arr = self.single_element_list.copy()
        self.quick_sort.simple_sort(arr)
        self.assertEqual(arr, [1])

    def test_should_simple_quick_sort_sorted(self):
        """
        Тестирование simple_sort на уже отсортированном массиве.
        """
        arr = self.sorted_list.copy()
        self.quick_sort.simple_sort(arr)
        self.assertEqual(arr, self.sorted_list)

    def test_should_simple_quick_sort_reverse(self):
        """
        Тестирование simple_sort на массиве, отсортированном в обратном порядке.
        """
        arr = self.reverse_sorted_list.copy()
        expected = sorted(self.reverse_sorted_list)
        self.quick_sort.simple_sort(arr)
        self.assertEqual(arr, expected)

    def test_should_simple_quick_sort_random(self):
        """
        Тестирование simple_sort на случайном массиве.
        """
        arr = self.random_list.copy()
        expected = sorted(self.random_list)
        self.quick_sort.simple_sort(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_duplicates(self):
        """
        Тестирование randomized_sort на массиве с дубликатами.
        """
        arr = self.duplicate_list.copy()
        expected = sorted(self.duplicate_list)
        self.quick_sort.randomized_sort(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_all_same(self):
        """
        Тестирование randomized_sort на массиве, состоящем из одинаковых элементов.
        """
        arr = self.all_same.copy()
        expected = sorted(self.all_same)
        self.quick_sort.randomized_sort(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_partition3_empty(self):
        """
        Тестирование randomized_sort_partition3 на пустом массиве.
        """
        arr = self.empty_list.copy()
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, [])

    def test_should_randomized_quick_sort_partition3_single(self):
        """
        Тестирование randomized_sort_partition3 на массиве с одним элементом.
        """
        arr = self.single_element_list.copy()
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, [1])

    def test_should_randomized_quick_sort_partition3_sorted(self):
        """
        Тестирование randomized_sort_partition3 на уже отсортированном массиве.
        """
        arr = self.sorted_list.copy()
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, self.sorted_list)

    def test_should_randomized_quick_sort_partition3_reverse(self):
        """
        Тестирование randomized_sort_partition3 на массиве, отсортированном в обратном порядке.
        """
        arr = self.reverse_sorted_list.copy()
        expected = sorted(self.reverse_sorted_list)
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_partition3_random(self):
        """
        Тестирование randomized_sort_partition3 на случайном массиве.
        """
        arr = self.random_list.copy()
        expected = sorted(self.random_list)
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_partition3_duplicates(self):
        """
        Тестирование randomized_sort_partition3 на массиве с дубликатами.
        """
        arr = self.duplicate_list.copy()
        expected = sorted(self.duplicate_list)
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, expected)

    def test_should_randomized_quick_sort_partition3_all_same(self):
        """
        Тестирование randomized_sort_partition3 на массиве, состоящем из одинаковых элементов.
        """
        arr = self.all_same.copy()
        expected = sorted(self.all_same)
        self.quick_sort.randomized_sort_partition3(arr)
        self.assertEqual(arr, expected)

    def test_should_merge_sort_empty(self):
        """
        Тестирование merge_sort на пустом массиве.
        """
        arr = self.empty_list.copy()
        expected = []
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_single(self):
        """
        Тестирование merge_sort на массиве с одним элементом.
        """
        arr = self.single_element_list.copy()
        expected = [1]
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_sorted(self):
        """
        Тестирование merge_sort на уже отсортированном массиве.
        """
        arr = self.sorted_list.copy()
        expected = self.sorted_list.copy()
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_reverse(self):
        """
        Тестирование merge_sort на массиве, отсортированном в обратном порядке.
        """
        arr = self.reverse_sorted_list.copy()
        expected = sorted(self.reverse_sorted_list)
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_random(self):
        """
        Тестирование merge_sort на случайном массиве.
        """
        arr = self.random_list.copy()
        expected = sorted(self.random_list)
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_duplicates(self):
        """
        Тестирование merge_sort на массиве с дубликатами.
        """
        arr = self.duplicate_list.copy()
        expected = sorted(self.duplicate_list)
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)

    def test_should_merge_sort_all_same(self):
        """
        Тестирование merge_sort на массиве, состоящем из одинаковых элементов.
        """
        arr = self.all_same.copy()
        expected = self.all_same.copy()
        result = self.merge_sort.sort(arr)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
