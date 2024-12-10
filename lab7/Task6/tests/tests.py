import unittest
from lab7.Task6.src.LISFinder import LISFinder

class TestFindLIS(unittest.TestCase):

    def test_simple_case(self):
        n = 5
        sequence = [10, 20, 10, 30, 20]
        lis_length, lis_sequence = LISFinder.find_lis(sequence)
        self.assertEqual(lis_length, 3)
        self.assertEqual(lis_sequence, [10, 20, 30])

    def test_sorted_sequence(self):
        sequence = [1, 2, 3, 4]
        lis_length, lis_sequence = LISFinder.find_lis(sequence)
        self.assertEqual(lis_length, 4)
        self.assertEqual(lis_sequence, [1, 2, 3, 4])

    def test_reversed_sequence(self):
        sequence = [4, 3, 2, 1]
        lis_length, lis_sequence = LISFinder.find_lis(sequence)
        self.assertEqual(lis_length, 1)
        self.assertEqual(lis_sequence, [1])

    def test_all_equal(self):
        sequence = [7, 7, 7, 7, 7]
        lis_length, lis_sequence = LISFinder.find_lis(sequence)
        self.assertEqual(lis_length, 1)
        self.assertEqual(lis_sequence, [7])


if __name__ == "__main__":
    unittest.main()
