import unittest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """
    Тесты для пузырьковой сортировки.
    """

    def test_bubble_sort(self):
        """
        Проверка корректности работы пузырьковой сортировки.
        """
        self.assertEqual(bubble_sort([31, 41, 59, 26, 41, 58]), [26, 31, 41, 41, 58, 59])

if __name__ == '__main__':
    unittest.main()
