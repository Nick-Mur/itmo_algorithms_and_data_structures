"""
Модуль с тестами для AntiQuickSortGenerator.
"""

import unittest
from Lab3.Task2.src.AntiQuickSortGenerator import AntiQuickSortGenerator


class TestAntiQuickSortGenerator(unittest.TestCase):
    """
    Класс для тестирования AntiQuickSortGenerator.
    """

    def test_should_n_0(self):
        n = 0
        expected = []
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_1(self):
        n = 1
        expected = [1]
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_2(self):
        n = 2
        expected = [1, 2]
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_3(self):
        n = 3
        expected = [1, 3, 2]
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_4(self):
        n = 4
        expected = [1, 4, 2, 3]
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_5(self):
        n = 5
        expected = [1, 4, 5, 3, 2]
        result = AntiQuickSortGenerator.generate(n)
        self.assertEqual(result, expected)

    def test_should_n_large(self):
        n = 1000
        result = AntiQuickSortGenerator.generate(n)
        # Проверяем, что результат является перестановкой чисел от 1 до n
        self.assertEqual(sorted(result), list(range(1, n + 1)))
        # Проверяем длину
        self.assertEqual(len(result), n)


if __name__ == '__main__':
    unittest.main()
