import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from insertion_sort_with_indexes import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """
    Тесты для функции сортировки вставками.
    """

    def test_insertion_sort(self):
        """
        Проверка корректности работы сортировки вставками.
        """
        sorted_indexes, sorted_arr = insertion_sort([1, 8, 4, 2, 3, 7, 5, 6, 9, 0])
        self.assertEqual(sorted_arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sorted_indexes, [1, 2, 2, 2, 3, 5, 5, 6, 9, 1])

if __name__ == '__main__':
    unittest.main()
