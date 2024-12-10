# Lab2/Task5/tests/tests.py

import unittest
from lab2.Task5.src.MajorityElementFinder import MajorityElementFinder

class TestMajorityElement(unittest.TestCase):

    def test_exists(self):
        array=[2,3,9,2,2]
        self.assertEqual(MajorityElementFinder.majority_element(array),2)

    def test_no_majority(self):
        array=[1,2,3,4]
        self.assertIsNone(MajorityElementFinder.majority_element(array))

if __name__=='__main__':
    unittest.main()
