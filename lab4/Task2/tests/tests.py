# Task2/tests/tests.py

"""Тесты для QueueProcessor."""

import unittest
from lab4.Task2.src.QueueProcessor import QueueProcessor


class TestQueueProcessor(unittest.TestCase):
    """Класс для тестирования QueueProcessor."""

    def test_should_process_queue_with_simple(self):
        """Тест с простым случаем."""
        commands = ["+ 5", "-"]
        processor = QueueProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [5])

    def test_should_process_queue_with_multiple(self):
        """Тест с несколькими операциями."""
        commands = ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-"]
        processor = QueueProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [1, 10])

    def test_should_process_queue_with_large_numbers(self):
        """Тест с большими числами."""
        commands = ["+ 1000000000", "+ -1000000000", "-", "-"]
        processor = QueueProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [1000000000, -1000000000])

    def test_should_process_queue_with_interleaved_operations(self):
        """Тест с чередующимися операциями."""
        commands = ["+ 7", "+ 14", "-", "+ 21", "+ 28", "-", "-"]
        processor = QueueProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [7, 14, 21])

    def test_should_process_queue_with_only_push(self):
        """Тест с только операциями добавления."""
        commands = ["+ 1", "+ 2", "+ 3"]
        processor = QueueProcessor()
        processor.process_commands(commands)
        self.assertEqual(processor.get_results(), [])

    def test_should_fail_with_invalid_command(self):
        """Тест с некорректной командой."""
        commands = ["+1", "-"]
        processor = QueueProcessor()
        self.assertFalse(processor.validate_commands(commands))

    def test_should_fail_with_large_number(self):
        """Тест с числом вне допустимого диапазона."""
        commands = ["+ 10000000000", "-"]
        processor = QueueProcessor()
        self.assertFalse(processor.validate_commands(commands))
