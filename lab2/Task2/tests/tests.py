# Lab2/Task2/tests/tests.py

import unittest
from lab2.Task2.src.MergeSorterWithIndices import MergeSorterWithIndices

class TestMergeSortWithIndices(unittest.TestCase):

    def test_basic_sort(self):
        array=[9,7,5,8]
        MergeSorterWithIndices.merge_sort_with_indices(array,0,len(array)-1)
        self.assertEqual(array,[5,7,8,9])

    def test_already_sorted(self):
        array=[1,2,3,4]
        MergeSorterWithIndices.merge_sort_with_indices(array,0,len(array)-1)
        self.assertEqual(array,[1,2,3,4])


if __name__=='__main__':
    unittest.main()
