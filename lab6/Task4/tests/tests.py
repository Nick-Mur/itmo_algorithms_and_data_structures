# Lab5/Task4/tests/tests.py

import unittest
from lab6.Task4.src.AssocArrayProcessor import AssocArrayProcessor

class TestAssocArrayProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = AssocArrayProcessor()

    def test_put_and_get(self):
        commands = ["put key1 value1", "put key2 value2", "get key1", "get key2", "get key3"]
        result = self.processor.process_commands(commands)
        self.assertEqual(result, ["value1", "value2", "<none>"])

    def test_overwrite(self):
        commands = ["put key1 value1", "put key1 value2", "get key1"]
        result = self.processor.process_commands(commands)
        self.assertEqual(result, ["value2"])

    def test_prev_and_next(self):
        commands = [
            "put key1 value1",
            "put key2 value2",
            "put key3 value3",
            "prev key2",
            "next key2",
            "prev key1",
            "next key3",
        ]
        result = self.processor.process_commands(commands)
        self.assertEqual(result, ["value1", "value3", "<none>", "<none>"])

    def test_delete(self):
        commands = ["put key1 value1", "put key2 value2", "delete key1", "get key1", "get key2"]
        result = self.processor.process_commands(commands)
        self.assertEqual(result, ["<none>", "value2"])

    def test_empty(self):
        commands = []
        result = self.processor.process_commands(commands)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
