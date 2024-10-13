import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from inversions_count import merge_sort_and_count



class TestInversionsCount(unittest.TestCase):

    def test_inversions(self):
        array = [1, 20, 6, 4, 5]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 5)

    def test_no_inversions(self):
        array = [1, 2, 3, 4, 5]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 0)

    def test_reverse_sorted(self):
        array = [5, 4, 3, 2, 1]
        temp_array = [0] * len(array)
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 10)

    def test_empty_array(self):
        array = []
        temp_array = []
        result = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
        self.assertEqual(result, 0)

    def test_invalid_arguments(self):
        # Тесты для некорректных типов аргументов
        with self.assertRaises(TypeError):
            merge_sort_and_count(None, [], 0, 1)
        with self.assertRaises(TypeError):
            merge_sort_and_count("not an array", [], 0, 1)

        # Тесты для некорректных размеров временного массива
        with self.assertRaises(ValueError):
            merge_sort_and_count([1, 2, 3], [], 0, 2)  # Временный массив слишком мал
        with self.assertRaises(ValueError):
            merge_sort_and_count([1, 2, 3], [], 1, 10)  # Временный массив слишком мал


if __name__ == '__main__':
    unittest.main()
