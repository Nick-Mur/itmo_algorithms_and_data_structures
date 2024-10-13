import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from majority_element import majority_element


class TestMajorityElement(unittest.TestCase):

    def test_majority_element_exists(self):
        array = [2, 3, 9, 2, 2]
        self.assertEqual(majority_element(array), 2)

    def test_no_majority_element(self):
        array = [1, 2, 3, 4]
        self.assertIsNone(majority_element(array))

    def test_single_element(self):
        array = [1]
        self.assertEqual(majority_element(array), 1)

    def test_empty_array(self):
        array = []
        self.assertIsNone(majority_element(array))

    def test_majority_element_boundary(self):
        array = [1, 1, 2, 1, 2, 1]
        self.assertEqual(majority_element(array), 1)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            majority_element(None)
        with self.assertRaises(TypeError):
            majority_element("not an array")


if __name__ == '__main__':
    unittest.main()
