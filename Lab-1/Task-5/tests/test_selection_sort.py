import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    """
    Тесты для функции сортировки выбором.
    """

    def test_selection_sort(self):
        """
        Проверка корректности работы сортировки выбором.
        """
        self.assertEqual(selection_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()
