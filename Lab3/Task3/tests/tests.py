"""
Модуль с тестами для ScarecrowSortChecker.
"""

import unittest
from Lab3.Task3.src.ScarecrowSortChecker import ScarecrowSortChecker

class TestScarecrowSortChecker(unittest.TestCase):
    """
    Класс для тестирования ScarecrowSortChecker.
    """

    def test_should_example1(self):
        n = 3
        k = 2
        arr = [2, 1, 3]
        expected = False
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_example2(self):
        n = 5
        k = 3
        arr = [1, 5, 3, 4, 1]
        expected = True
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_already_sorted(self):
        n = 4
        k = 1
        arr = [1, 2, 3, 4]
        expected = True
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_single_element(self):
        n = 1
        k = 1
        arr = [10]
        expected = True
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_unsortable(self):
        n = 4
        k = 2
        arr = [4, 3, 2, 1]
        expected = False
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_large_k(self):
        n = 6
        k = 3
        arr = [3, 1, 2, 6, 4, 5]
        expected = False
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_large_n(self):
        n = 100000
        k = 50000
        arr = list(range(1, n + 1))
        expected = True
        result = ScarecrowSortChecker.can_sort(n, k, arr)
        self.assertEqual(result, expected)

    def test_should_invalid_input_length(self):
        n = 3
        k = 1
        arr = [1, 2]
        with self.assertRaises(ValueError):
            ScarecrowSortChecker.can_sort(n, k, arr)

if __name__ == '__main__':
    unittest.main()
