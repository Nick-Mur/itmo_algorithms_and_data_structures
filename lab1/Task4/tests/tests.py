# Lab1/Task4/tests/tests.py

import unittest
from lab1.Task4.src.LinearSearcher import LinearSearcher

class TestLinearSearch(unittest.TestCase):
    def test_linear_search(self):
        self.assertEqual(LinearSearcher.linear_search([10,20,30,40],30), ['3'])
        self.assertEqual(LinearSearcher.linear_search([10,20,30,40],50), ['-1'])
        self.assertEqual(LinearSearcher.linear_search([10,20,30,40,40],40), ['4','5'])

if __name__=='__main__':
    unittest.main()
