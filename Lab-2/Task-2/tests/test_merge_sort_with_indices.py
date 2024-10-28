import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort_with_indices import merge_sort_with_indices


class TestMergeSortWithIndices(unittest.TestCase):

    def test_should_basic_sort_with_indices(self):
        array = [9, 7, 5, 8]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [5, 7, 8, 9])

    def test_should_already_sorted(self):
        array = [1, 2, 3, 4]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 4])

    def test_should_reverse_sorted(self):
        array = [10, 9, 8, 7]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [7, 8, 9, 10])

    def test_should_single_element(self):
        array = [1]
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [1])

    def test_should_empty_array(self):
        array = []
        merge_sort_with_indices(array, 0, len(array) - 1)
        self.assertEqual(array, [])

    def test_should_invalid_arguments(self):
        with self.assertRaises(TypeError):
            merge_sort_with_indices(None, 0, 1)
        with self.assertRaises(TypeError):
            merge_sort_with_indices("not an array", 0, 1)
        with self.assertRaises(ValueError):
            merge_sort_with_indices([1, 2, 3], -1, 2)  # Некорректные индексы
        with self.assertRaises(ValueError):
            merge_sort_with_indices([1, 2, 3], 1, 10)  # Индекс выходит за пределы массива


if __name__ == '__main__':
    unittest.main()
