# Lab5/Task2/tests/tests.py

import unittest
from lab5.Task2.src.TreeHeightCalculator import TreeHeightCalculator


class TestTreeHeightCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = TreeHeightCalculator()

    def test_simple_case(self):
        n = 5
        parents = [4, -1, 4, 1, 1]  # Ожидаемая высота 3
        result = self.calc.tree_height(n, parents)
        self.assertEqual(result, 3)

    def test_another_case(self):
        n = 5
        parents = [-1, 0, 4, 0, 3] # Высота 4
        result = self.calc.tree_height(n, parents)
        self.assertEqual(result, 4)

    def test_binary_tree(self):
        n = 7
        parents = [-1, 0, 0, 1, 1, 2, 2] # Высота 3
        result = self.calc.tree_height(n, parents)
        self.assertEqual(result, 3)

    def test_deep_tree(self):
        n = 10
        parents = [-1,0,1,2,3,4,5,6,7,8] # Линейное дерево, высота 10
        result = self.calc.tree_height(n, parents)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
