import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from insertion_sort_with_indexes import insertion_sort_with_indexes


class TestInsertionSortWithIndexes(unittest.TestCase):
    """
    Тесты для сортировки вставками с отслеживанием индексов.
    """

    def test_insertion_sort_with_indexes(self):
        """
        Проверка корректности работы сортировки вставками с индексами.
        """
        self.assertEqual(insertion_sort_with_indexes([8, 4, 2, 3, 7, 5, 6, 9, 0]), [8, 2, 3, 1, 5, 6, 4, 0, 7])

if __name__ == '__main__':
    unittest.main()
