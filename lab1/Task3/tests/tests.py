# Lab1/Task3/tests/tests.py

import unittest
from lab1.Task3.src.InsertionSorterDescending import InsertionSorterDescending

class TestInsertionSortDescending(unittest.TestCase):
    def test_insertion_sort_descending(self):
        self.assertEqual(InsertionSorterDescending.insertion_sort_descending([31,41,59,26,41,58]),
                         [59,58,41,41,31,26])
        self.assertEqual(InsertionSorterDescending.insertion_sort_descending([]), [])
        self.assertEqual(InsertionSorterDescending.insertion_sort_descending([1]), [1])

if __name__=='__main__':
    unittest.main()
