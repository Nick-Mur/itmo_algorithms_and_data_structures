# Lab5/Task7/tests/tests.py

import unittest
from lab5.Task7.src.HeapSorter import HeapSorter

class TestHeapSorter(unittest.TestCase):

    def setUp(self):
        self.sorter = HeapSorter()

    def test_heapify(self):
        arr = [3, 9, 2, 1, 4]
        self.sorter.heapify(arr, len(arr), 0)
        self.assertEqual(arr, [9, 4, 2, 1, 3])

    def test_heapsort_sorted(self):
        arr = [5,4,3,2,1]
        self.sorter.heapsort(arr)
        self.assertEqual(arr, [1,2,3,4,5])

    def test_heapsort_random(self):
        arr = [4,10,3,5,1]
        self.sorter.heapsort(arr)
        self.assertEqual(arr, [1,3,4,5,10])

    def test_heapsort_reverse_sorted(self):
        arr = [5,4,3,2,1]
        self.sorter.heapsort(arr)
        self.assertEqual(arr, [1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()
