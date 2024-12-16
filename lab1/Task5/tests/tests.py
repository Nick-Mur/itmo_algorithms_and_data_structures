# Lab1/Task5/tests/tests.py

import unittest
from lab1.Task5.src.SelectionSorter import SelectionSorter

class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(SelectionSorter.selection_sort([31,41,59,26,41,58]),
                         [26,31,41,41,58,59])
        self.assertEqual(SelectionSorter.selection_sort([]), [])
        self.assertEqual(SelectionSorter.selection_sort([1]), [1])
        self.assertEqual(SelectionSorter.selection_sort([2,1]), [1,2])

if __name__=='__main__':
    unittest.main()
