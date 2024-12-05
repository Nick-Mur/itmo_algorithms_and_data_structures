# Task8/tests/tests.py

"""Тесты для PostfixEvaluator."""

import unittest
from lab4.Task8.src.PostfixEvaluator import PostfixEvaluator


class TestPostfixEvaluator(unittest.TestCase):
    """Класс для тестирования PostfixEvaluator."""

    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.evaluator = PostfixEvaluator()

    def test_should_work_with_basic_operations(self):
        """Тест базовых операций."""
        expressions = [
            (["2", "3", "+"], 5),
            (["10", "4", "-"], 6),
            (["6", "7", "*"], 42),
        ]

        for expr, expected in expressions:
            with self.subTest(expr=expr):
                self.assertEqual(self.evaluator.evaluate_postfix(expr), expected)

    def test_should_work_with_complex_expression(self):
        """Тест сложного выражения."""
        expression = ["2", "3", "+", "4", "*", "5", "+"]
        result = self.evaluator.evaluate_postfix(expression)
        self.assertEqual(result, 25)

    def test_should_work_with_large_numbers(self):
        """Тест с большими числами."""
        expression = ["2147483646", "1", "+"]
        result = self.evaluator.evaluate_postfix(expression)
        self.assertEqual(result, 2147483647)

    def test_should_work_with_invalid_operator(self):
        """Тест с недопустимым оператором."""
        expression = ["2", "3", "&"]
        with self.assertRaises(ValueError) as context:
            self.evaluator.evaluate_postfix(expression)
        self.assertIn("Неизвестный оператор", str(context.exception))

    def test_should_work_with_intermediate_overflow(self):
        """Тест с переполнением промежуточного результата."""
        expression = ["1073741824", "2", "*"]
        with self.assertRaises(ValueError) as context:
            self.evaluator.evaluate_postfix(expression)
        self.assertIn("Промежуточный результат превышает предел", str(context.exception))

    def test_should_work_with_number_out_of_bounds(self):
        """Тест с числом вне допустимых границ."""
        expression = ["2147483648"]
        with self.assertRaises(ValueError) as context:
            self.evaluator.evaluate_postfix(expression)
        self.assertIn("выходящее за пределы", str(context.exception))

    def test_should_work_with_empty_expression(self):
        """Тест с пустым выражением."""
        expression = []
        with self.assertRaises(IndexError):
            self.evaluator.evaluate_postfix(expression)

    def test_should_work_with_unbalanced_expression(self):
        """Тест с несбалансированным выражением."""
        expression = ["2", "+"]
        with self.assertRaises(IndexError):
            self.evaluator.evaluate_postfix(expression)

    def test_should_valid_with_zeros(self):
        """Тест с нулями."""
        expression = ["0", "0", "+", "0", "*"]
        result = self.evaluator.evaluate_postfix(expression)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
