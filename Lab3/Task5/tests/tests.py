"""
Модуль с тестами для HIndexCalculator.
"""

import unittest
from Lab3.Task5.src.HIndexCalculator import HIndexCalculator

class TestHIndexCalculator(unittest.TestCase):
    """
    Класс для тестирования HIndexCalculator.
    """

    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_case_2(self):
        citations = [1, 3, 1]
        expected = 1
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_empty_citations(self):
        citations = []
        expected = 0
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_all_zero_citations(self):
        citations = [0, 0, 0]
        expected = 0
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_high_h_index(self):
        citations = [100, 100, 100, 100]
        expected = 4
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_h_index_equals_number_of_papers(self):
        citations = [1, 1, 1, 1, 1]
        expected = 1
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_large_number_of_papers(self):
        citations = list(range(1, 1001))  # 1, 2, 3, ..., 1000
        expected = 500  # The H-index is the maximum h such that h papers have at least h citations
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_single_paper_no_citations(self):
        citations = [0]
        expected = 0
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

    def test_single_paper_with_citations(self):
        citations = [10]
        expected = 1
        result = HIndexCalculator.calculate_h_index(citations)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
