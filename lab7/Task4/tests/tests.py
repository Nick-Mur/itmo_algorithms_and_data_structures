import unittest
from lab7.Task4.src.LCSFinder import LCSFinder

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_with_common_elements(self):
        A = [2, 7, 5]
        B = [2, 5]
        self.assertEqual(LCSFinder.longest_common_subsequence(A, B), 2)

    def test_no_common_elements(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        self.assertEqual(LCSFinder.longest_common_subsequence(A, B), 0)

    def test_identical_sequences(self):
        A = [1, 2, 3, 4]
        B = [1, 2, 3, 4]
        self.assertEqual(LCSFinder.longest_common_subsequence(A, B), 4)

    def test_one_empty_sequence(self):
        A = []
        B = [1,2,3,4,5]
        self.assertEqual(LCSFinder.longest_common_subsequence(A, B), 0)

    def test_repeated_elements(self):
        A = [1, 2, 2, 3, 4]
        B = [2, 2, 4, 5]
        self.assertEqual(LCSFinder.longest_common_subsequence(A, B), 3)


if __name__ == "__main__":
    unittest.main()
