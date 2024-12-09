"""Тесты для BracketSequenceChecker."""

import unittest
from lab4.Task3.src.BracketSequenceChecker import BracketSequenceChecker


class TestBracketSequenceChecker(unittest.TestCase):
    """Класс для тестирования BracketSequenceChecker."""

    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.checker = BracketSequenceChecker()

    def test_empty_sequence(self):
        """Тест пустой строки."""
        sequence = ""
        result = self.checker.is_valid_sequence(sequence)
        self.assertTrue(result)

    def test_single_type_brackets(self):
        """Тест последовательностей с одним типом скобок."""
        self.assertTrue(self.checker.is_valid_sequence("()"))
        self.assertTrue(self.checker.is_valid_sequence("(())"))
        self.assertFalse(self.checker.is_valid_sequence("(()"))
        self.assertFalse(self.checker.is_valid_sequence("())"))

    def test_mixed_brackets(self):
        """Тест смешанных типов скобок."""
        self.assertTrue(self.checker.is_valid_sequence("()[]"))
        self.assertTrue(self.checker.is_valid_sequence("([])"))
        self.assertFalse(self.checker.is_valid_sequence("([)]"))
        self.assertFalse(self.checker.is_valid_sequence("[(])"))

    def test_nested_brackets(self):
        """Тест вложенных скобок."""
        self.assertTrue(self.checker.is_valid_sequence("(([]))"))
        self.assertTrue(self.checker.is_valid_sequence("[([])]"))
        self.assertFalse(self.checker.is_valid_sequence("(([])"))
        self.assertFalse(self.checker.is_valid_sequence("(([])))"))

    def test_unbalanced_brackets(self):
        """Тест несбалансированных скобок."""
        self.assertFalse(self.checker.is_valid_sequence("("))
        self.assertFalse(self.checker.is_valid_sequence(")"))
        self.assertFalse(self.checker.is_valid_sequence("["))
        self.assertFalse(self.checker.is_valid_sequence("]"))

    def test_large_sequence(self):
        """Тест больших последовательностей."""
        sequence_valid = "()" * 5000
        sequence_invalid = "(" * 5000 + ")" * 4999
        self.assertTrue(self.checker.is_valid_sequence(sequence_valid))
        self.assertFalse(self.checker.is_valid_sequence(sequence_invalid))

    def test_validate_input(self):
        """Тест валидации входных данных."""
        n = 2
        sequences = ["()", "[]"]
        self.assertTrue(self.checker.validate_input(n, sequences))

        n = 0
        sequences = []
        self.assertFalse(self.checker.validate_input(n, sequences))

        n = 501
        sequences = ["()"] * 501
        self.assertFalse(self.checker.validate_input(n, sequences))

        n = 2
        sequences = ["", "[]"]
        self.assertFalse(self.checker.validate_input(n, sequences))

        n = 2
        sequences = ["(" * (10**4 + 1), "[]"]
        self.assertFalse(self.checker.validate_input(n, sequences))


if __name__ == '__main__':
    unittest.main()
