import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    """
    Тесты для функции линейного поиска.
    """

    def test_linear_search(self):
        """
        Проверка корректности работы линейного поиска.
        """
        self.assertEqual(linear_search([10, 20, 30, 40], 30), [2])
        self.assertEqual(linear_search([10, 20, 30, 40], 50), -1)

if __name__ == '__main__':
    unittest.main()