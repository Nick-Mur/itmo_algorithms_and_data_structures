import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from insertion_sort import insertion_sort



class TestInsertionSort(unittest.TestCase):
    """
    Тесты для функции сортировки вставками.
    """

    def test_insertion_sort(self):
        """
        Проверка корректности работы сортировки вставками.
        """
        self.assertEqual(insertion_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()
