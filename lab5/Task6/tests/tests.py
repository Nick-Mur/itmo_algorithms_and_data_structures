# Lab5/Task6/tests/tests.py

import unittest
from lab5.Task6.src.PriorityQueueProcessor import PriorityQueueProcessor

class TestPriorityQueueProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PriorityQueueProcessor()

    def test_add_and_extract_min(self):
        operations = ["A 5", "A 3", "A 7", "X", "X", "X"]
        result = self.processor.process_operations(operations)
        self.assertEqual(result, ["3", "5", "7"])

    def test_extract_from_empty(self):
        operations = ["X", "X"]
        result = self.processor.process_operations(operations)
        self.assertEqual(result, ["*", "*"])

    def test_decrease_key(self):
        operations = ["A 10", "A 15", "A 20", "D 1 5", "X", "X", "X"]
        result = self.processor.process_operations(operations)
        self.assertEqual(result, ["5", "10", "20"])

    def test_large_numbers(self):
        operations = ["A 1000000000", "A -1000000000", "X", "X", "X"]
        result = self.processor.process_operations(operations)
        self.assertEqual(result, ["-1000000000", "1000000000", "*"])


if __name__ == '__main__':
    unittest.main()
