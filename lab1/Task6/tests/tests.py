# Lab1/Task6/tests/tests.py

import unittest
from lab1.Task6.src.BubbleSorter import BubbleSorter

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(BubbleSorter.bubble_sort([31,41,59,26,41,58]),
                         [26,31,41,41,58,59])
        self.assertEqual(BubbleSorter.bubble_sort([]), [])
        self.assertEqual(BubbleSorter.bubble_sort([1]), [1])
        self.assertEqual(BubbleSorter.bubble_sort([2,1]), [1,2])

if __name__=='__main__':
    unittest.main()
