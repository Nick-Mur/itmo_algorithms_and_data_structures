# Lab4/Task13/tests/test_stack.py

import unittest
from lab4.Task13.src.Stack import Stack
from io import StringIO
from unittest.mock import patch

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.stack.isEmpty())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(self.stack.display(), None)
            self.assertEqual(fake_out.getvalue(), "")

    def test_push_pop(self):
        self.stack.push(10)
        self.assertFalse(self.stack.isEmpty())

        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 10)
        self.assertTrue(self.stack.isEmpty())


if __name__ == '__main__':
    unittest.main()
