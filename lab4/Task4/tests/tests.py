# Task4/tests/tests.py

"""Тесты для BracketChecker."""

import unittest
from lab4.Task4.src.BracketChecker import BracketChecker


class TestBracketChecker(unittest.TestCase):
    """Класс для тестирования BracketChecker."""

    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.checker = BracketChecker()

    def test_should_return_success_for_correct_sequence(self):
        """Тест с корректной последовательностью."""
        data = "([]){()}"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "Success")

    def test_should_return_error_index_for_incorrect_sequence(self):
        """Тест с некорректной последовательностью."""
        data = "{[}"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "3")

    def test_should_return_error_index_for_unmatched_closing_bracket(self):
        """Тест с лишней закрывающей скобкой."""
        data = "foo(bar);)"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "10")

    def test_should_return_error_index_for_unmatched_opening_bracket(self):
        """Тест с незакрытой открывающей скобкой."""
        data = "([]"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "1")

    def test_should_handle_empty_string(self):
        """Тест с пустой строкой."""
        data = ""
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "Success")

    def test_should_handle_no_brackets(self):
        """Тест со строкой без скобок."""
        data = "Hello, World!"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "Success")

    def test_should_handle_complex_sequence(self):
        """Тест со сложной последовательностью."""
        data = "([](){([])})"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "Success")

    def test_should_return_error_for_incorrect_nested_sequence(self):
        """Тест с некорректно вложенной последовательностью."""
        data = "({[}])"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "4")

    def test_should_return_error_for_unmatched_opening_bracket_at_start(self):
        """Тест с незакрытой открывающей скобкой в начале."""
        data = "{"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "1")

    def test_should_return_error_for_unmatched_closing_bracket_at_start(self):
        """Тест с лишней закрывающей скобкой в начале."""
        data = "}"
        result = self.checker.check_brackets(data)
        self.assertEqual(result, "1")


if __name__ == '__main__':
    unittest.main()
