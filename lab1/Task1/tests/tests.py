# Lab1/Task1/tests/tests.py

import unittest
from lab1.Task1.src.InsertionSorter import InsertionSorter

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(InsertionSorter.insertion_sort([31,41,59,26,41,58]), [26,31,41,41,58,59])
        self.assertEqual(InsertionSorter.insertion_sort([]), [])
        self.assertEqual(InsertionSorter.insertion_sort([1]), [1])
        self.assertEqual(InsertionSorter.insertion_sort([2,1]), [1,2])
        self.assertEqual(InsertionSorter.insertion_sort([1,2,3]), [1,2,3])

if __name__=='__main__':
    unittest.main()
