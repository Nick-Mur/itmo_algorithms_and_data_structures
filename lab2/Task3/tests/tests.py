# Lab2/Task3/tests/tests.py

import unittest
from lab2.Task3.src.InversionsCounter import InversionsCounter

class TestInversionsCount(unittest.TestCase):

    def test_inversions(self):
        array=[1,20,6,4,5]
        temp=[0]*len(array)
        result=InversionsCounter.merge_sort_and_count(array,temp,0,len(array)-1)
        self.assertEqual(result,5)

    def test_no_inversions(self):
        array=[1,2,3,4,5]
        temp=[0]*len(array)
        result=InversionsCounter.merge_sort_and_count(array,temp,0,len(array)-1)
        self.assertEqual(result,0)


if __name__=='__main__':
    unittest.main()
