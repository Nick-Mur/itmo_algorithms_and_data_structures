import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from insertion_sort_descending import insertion_sort_descending


class TestInsertionSortDescending(unittest.TestCase):
    """
    Тесты для сортировки вставками по убыванию.
    """

    def test_insertion_sort_descending(self):
        """
        Проверка корректности работы сортировки вставками по убыванию.
        """
        self.assertEqual(insertion_sort_descending([31, 41, 59, 26, 41, 58]), [59, 58, 41, 41, 31, 26])

if __name__ == '__main__':
    unittest.main()
