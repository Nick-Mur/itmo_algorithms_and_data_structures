# Lab2/Task6/tests/tests.py

import unittest
from lab2.Task6.src.SortPerformanceTester import Sorter

class TestSortingAlgorithms(unittest.TestCase):

    def test_empty_array(self):
        arr=[]
        self.assertEqual(Sorter.merge_sort(arr),[])
        self.assertEqual(Sorter.insertion_sort(arr),[])
        self.assertEqual(Sorter.selection_sort(arr),[])

    def test_single_element(self):
        arr=[1]
        self.assertEqual(Sorter.merge_sort(arr),[1])
        self.assertEqual(Sorter.insertion_sort(arr),[1])
        self.assertEqual(Sorter.selection_sort(arr),[1])

    def test_sorted_array(self):
        arr=[1,2,3,4,5]
        self.assertEqual(Sorter.merge_sort(arr),[1,2,3,4,5])
        self.assertEqual(Sorter.insertion_sort(arr),[1,2,3,4,5])
        self.assertEqual(Sorter.selection_sort(arr),[1,2,3,4,5])

    def test_reverse_sorted_array(self):
        arr=[5,4,3,2,1]
        self.assertEqual(Sorter.merge_sort(arr),[1,2,3,4,5])
        self.assertEqual(Sorter.insertion_sort(arr),[1,2,3,4,5])
        self.assertEqual(Sorter.selection_sort(arr),[1,2,3,4,5])

    def test_random_array(self):
        arr=[3,1,4,5,2]
        expected=[1,2,3,4,5]
        self.assertEqual(Sorter.merge_sort(arr),expected)
        self.assertEqual(Sorter.insertion_sort(arr),expected)
        self.assertEqual(Sorter.selection_sort(arr),expected)

    def test_duplicates(self):
        arr=[3,1,2,3,1]
        expected=[1,1,2,3,3]
        self.assertEqual(Sorter.merge_sort(arr),expected)
        self.assertEqual(Sorter.insertion_sort(arr),expected)
        self.assertEqual(Sorter.selection_sort(arr),expected)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Sorter.merge_sort(None)
        with self.assertRaises(TypeError):
            Sorter.insertion_sort(None)
        with self.assertRaises(TypeError):
            Sorter.selection_sort(None)

if __name__=='__main__':
    unittest.main()
