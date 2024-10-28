import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_should_basic_sort(self):
        array = [12, 11, 13, 5, 6, 7]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [5, 6, 7, 11, 12, 13])

    def test_should_already_sorted(self):
        array = [1, 2, 3, 4, 5]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def test_should_reverse_sorted(self):
        array = [5, 4, 3, 2, 1]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def test_should_single_element(self):
        array = [1]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [1])

    def test_should_empty_array(self):
        array = []
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [])

    def test_should_large_numbers(self):
        array = [1000000000, 999999999, 999999998]
        merge_sort(array, 0, len(array) - 1)
        self.assertEqual(array, [999999998, 999999999, 1000000000])

    def test_should_invalid_arguments(self):
        with self.assertRaises(TypeError):
            merge_sort(None, 0, 1)
        with self.assertRaises(TypeError):
            merge_sort("not an array", 0, 1)
        with self.assertRaises(ValueError):
            merge_sort([1, 2, 3], -1, 2)  # Здесь вылетит ValueError
        with self.assertRaises(ValueError):
            merge_sort([1, 2, 3], 1, 10)  # Здесь вылетит ValueError

    def test_should_left_greater_than_right(self):
        # Случай, когда left > right, допустим, так что исключение не требуется
        array = [1, 2, 3]
        merge_sort(array, 2, 1)  # Функция должна завершить работу без действий
        self.assertEqual(array, [1, 2, 3])  # Массив не изменен


if __name__ == '__main__':
    unittest.main()
