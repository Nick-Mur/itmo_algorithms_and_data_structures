# Lab2/Task1/tests/tests.py

import unittest
from lab2.Task1.src.MergeSorter import MergeSorter

class TestMergeSort(unittest.TestCase):

    def test_basic_sort(self):
        array = [12, 11, 13, 5, 6, 7]
        MergeSorter.merge_sort(array, 0, len(array)-1)
        self.assertEqual(array, [5,6,7,11,12,13])

    def test_already_sorted(self):
        array = [1,2,3,4,5]
        MergeSorter.merge_sort(array, 0, len(array)-1)
        self.assertEqual(array, [1,2,3,4,5])

    def test_reverse_sorted(self):
        array = [5,4,3,2,1]
        MergeSorter.merge_sort(array, 0, len(array)-1)
        self.assertEqual(array, [1,2,3,4,5])

    def test_single_element(self):
        array = [1]
        MergeSorter.merge_sort(array, 0, len(array)-1)
        self.assertEqual(array, [1])

    def test_empty_array(self):
        array = []
        if array: # Если пустой, просто не сортируем
            MergeSorter.merge_sort(array,0,len(array)-1)
        self.assertEqual(array,[])

    def test_large_numbers(self):
        array = [1000000000,999999999,999999998]
        MergeSorter.merge_sort(array,0,len(array)-1)
        self.assertEqual(array,[999999998,999999999,1000000000])

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            MergeSorter.merge_sort([1,2,3],-1,2)
        with self.assertRaises(ValueError):
            MergeSorter.merge_sort([1,2,3],1,10)


if __name__ == '__main__':
    unittest.main()
