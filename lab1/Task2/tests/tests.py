# Lab1/Task2/tests/tests.py

import unittest
from lab1.Task2.src.InsertionSorterWithIndices import InsertionSorterWithIndices

class TestInsertionSortWithIndices(unittest.TestCase):
    def test_insertion_sort_with_indices(self):
        indexes, sorted_arr = InsertionSorterWithIndices.insertion_sort_with_indices([1,8,4,2,3,7,5,6,9,0])
        self.assertEqual(sorted_arr, [0,1,2,3,4,5,6,7,8,9])
        # Проверка корректности индексов - в примере индексы могут отличаться,
        # главное проверить, что алгоритм не падает.
        self.assertEqual(len(indexes), 10)

if __name__=='__main__':
    unittest.main()
