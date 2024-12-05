# Task1/tests/tests.py

"""Тесты для StackProcessor."""

import unittest
from lab4.Task1.src.StackProcessor import StackProcessor


class TestStackProcessor(unittest.TestCase):
    """Класс для тестирования StackProcessor."""

    def test_should_process_stack_with_simple(self):
        """Тест с простым случаем."""
        commands = ["+ 5", "-"]
        processor = StackProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [5])

    def test_should_process_stack_with_multiple(self):
        """Тест с несколькими операциями."""
        commands = ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-"]
        processor = StackProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [10, 1234])

    def test_should_process_stack_with_large_numbers(self):
        """Тест с большими числами."""
        commands = ["+ 1000000000", "+ -1000000000", "-", "-"]
        processor = StackProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [-1000000000, 1000000000])

    def test_should_process_stack_with_interleaved_operations(self):
        """Тест с чередующимися операциями."""
        commands = ["+ 7", "+ 14", "-", "+ 21", "+ 28", "-", "-"]
        processor = StackProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [14, 28, 21])

    def test_should_process_stack_with_only_push(self):
        """Тест с только операциями добавления."""
        commands = ["+ 1", "+ 2", "+ 3"]
        processor = StackProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [])

    def test_should_fail_with_invalid_command(self):
        """Тест с некорректной командой."""
        commands = ["+1", "-"]
        processor = StackProcessor()
        self.assertFalse(processor.validate_commands(commands))

    def test_should_fail_with_large_number(self):
        """Тест с числом вне допустимого диапазона."""
        commands = ["+ 10000000000", "-"]
        processor = StackProcessor()
        self.assertFalse(processor.validate_commands(commands))
