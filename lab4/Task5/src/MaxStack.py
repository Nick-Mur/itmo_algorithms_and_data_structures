# Task5/src/MaxStack.py

"""Модуль, реализующий стек с поддержкой операции max."""

from lab4.utils.IOHandler import IOHandler


class MaxStack:
    """
    Класс, реализующий стек с операцией получения максимума за O(1).
    """

    def __init__(self):
        """Инициализация стека и вспомогательного стека для максимумов."""
        self.stack = []
        self.max_stack = []

    def push(self, value):
        """
        Добавляет элемент на вершину стека.

        :param value: Значение для добавления.
        """
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        """
        Удаляет элемент с вершины стека.
        """
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()

    def max(self):
        """
        Возвращает максимальный элемент в стеке.

        :return: Максимальное значение или None, если стек пуст.
        """
        return self.max_stack[-1] if self.max_stack else None

    @staticmethod
    def read_commands(input_path):
        """
        Считывает команды из входного файла.

        :param input_path: Путь к входному файлу.
        :return: Количество команд и список команд.
        """
        lines = IOHandler.read_file(input_path)
        n = int(lines[0].strip())
        commands = [line.strip() for line in lines[1:]]
        return n, commands

    @staticmethod
    def validate_commands(n, commands):
        """
        Валидирует список команд.

        :param n: Количество команд.
        :param commands: Список команд.
        :return: True, если команды валидны, иначе False.
        """
        if not (1 <= n <= 400000):
            return False
        if len(commands) != n:
            return False
        for command in commands:
            if command.startswith("push"):
                parts = command.split()
                if len(parts) != 2:
                    return False
                try:
                    value = int(parts[1])
                    if not (0 <= value <= 100000):
                        return False
                except ValueError:
                    return False
            elif command not in ("pop", "max"):
                return False
        return True

    @staticmethod
    def write_results(output_path, results):
        """
        Записывает результаты в выходной файл.

        :param output_path: Путь к выходному файлу.
        :param results: Список результатов.
        """
        data = "\n".join(results)
        IOHandler.write_file(output_path, data)
