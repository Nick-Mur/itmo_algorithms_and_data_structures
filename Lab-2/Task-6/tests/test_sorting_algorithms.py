import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort_optimized import merge_sort, insertion_sort, selection_sort


class TestSortingAlgorithms(unittest.TestCase):

    def test_should_empty_array(self):
        arr = []
        self.assertEqual(merge_sort(arr.copy()), [])
        self.assertEqual(insertion_sort(arr.copy()), [])
        self.assertEqual(selection_sort(arr.copy()), [])

    def test_should_single_element(self):
        arr = [1]
        self.assertEqual(merge_sort(arr.copy()), [1])
        self.assertEqual(insertion_sort(arr.copy()), [1])
        self.assertEqual(selection_sort(arr.copy()), [1])

    def test_should_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(selection_sort(arr.copy()), [1, 2, 3, 4, 5])

    def test_should_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(selection_sort(arr.copy()), [1, 2, 3, 4, 5])

    def test_should_random_array(self):
        arr = [3, 1, 4, 5, 2]
        self.assertEqual(merge_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(arr.copy()), [1, 2, 3, 4, 5])
        self.assertEqual(selection_sort(arr.copy()), [1, 2, 3, 4, 5])

    def test_should_duplicates(self):
        arr = [3, 1, 2, 3, 1]
        self.assertEqual(merge_sort(arr.copy()), [1, 1, 2, 3, 3])
        self.assertEqual(insertion_sort(arr.copy()), [1, 1, 2, 3, 3])
        self.assertEqual(selection_sort(arr.copy()), [1, 1, 2, 3, 3])

    def test_should_invalid_arguments(self):
        with self.assertRaises(TypeError):
            merge_sort(None)
        with self.assertRaises(TypeError):
            insertion_sort(None)
        with self.assertRaises(TypeError):
            selection_sort(None)
        with self.assertRaises(TypeError):
            merge_sort("not a list")
        with self.assertRaises(TypeError):
            insertion_sort("not a list")
        with self.assertRaises(TypeError):
            selection_sort("not a list")

if __name__ == '__main__':
    unittest.main()
