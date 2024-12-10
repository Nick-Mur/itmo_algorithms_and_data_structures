import unittest
from lab7.Task5.src.LCS3Finder import LCS3Finder

class TestLongestCommonSubsequence3(unittest.TestCase):

    def test_common_subsequence_exists(self):
        a = [1, 2, 3]
        b = [2, 1, 3]
        c = [1, 3, 5]
        self.assertEqual(LCS3Finder.longest_common_subsequence_3(a, b, c), 2)

    def test_no_common_subsequence(self):
        a = [1,2,3]
        b = [4,5,6]
        c = [7,8,9]
        self.assertEqual(LCS3Finder.longest_common_subsequence_3(a, b, c), 0)

    def test_identical_sequences(self):
        a = [1,2,3]
        b = [1,2,3]
        c = [1,2,3]
        self.assertEqual(LCS3Finder.longest_common_subsequence_3(a, b, c), 3)

    def test_empty_sequences(self):
        a = []
        b = []
        c = []
        self.assertEqual(LCS3Finder.longest_common_subsequence_3(a, b, c), 0)

    def test_single_element_match(self):
        a = [1]
        b = [1]
        c = [1]
        self.assertEqual(LCS3Finder.longest_common_subsequence_3(a, b, c), 1)


if __name__ == "__main__":
    unittest.main()
