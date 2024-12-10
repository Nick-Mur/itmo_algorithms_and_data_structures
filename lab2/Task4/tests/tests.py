# Lab2/Task4/tests/tests.py

import unittest
from lab2.Task4.src.BinarySearcher import BinarySearcher

class TestBinarySearch(unittest.TestCase):

    def test_found(self):
        array=[1,2,3,4,5]
        self.assertEqual(BinarySearcher.binary_search(array,3),2)

    def test_not_found(self):
        array=[1,2,3,4,5]
        self.assertEqual(BinarySearcher.binary_search(array,6),-1)

if __name__=='__main__':
    unittest.main()
