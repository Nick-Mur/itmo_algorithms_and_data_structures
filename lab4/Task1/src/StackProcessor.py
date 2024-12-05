# Task1/src/StackProcessor.py

"""Модуль для обработки операций со стеком."""

from lab4.utils.IOHandler import IOHandler
from lab4.utils.consts import *
import os


class StackProcessor:
    """Класс для обработки команд работы со стеком."""

    def __init__(self):
        """Инициализация стека и результатов."""
        self.stack = []
        self.results = []

    def process_commands(self, commands):
        """
        Обрабатывает список команд и обновляет результаты.

        :param commands: Список команд.
        """
        for command in commands:
            if command.startswith("+"):
                _, number = command.split()
                self.stack.append(int(number))
            elif command == "-":
                self.results.append(self.stack.pop())

    @staticmethod
    def read_commands(input_path):
        """
        Считывает команды из файла.

        :param input_path: Путь к входному файлу.
        :return: Список команд.
        """
        lines = IOHandler.read_file(input_path)
        commands = [cmd.strip() for cmd in lines[1:]]  # Убираем первую строку и \n
        return commands

    @staticmethod
    def validate_commands(commands):
        """
        Валидирует список команд.

        :param commands: Список команд.
        :return: True если команды валидны, иначе False.
        """
        if not (1 <= len(commands) <= 10 ** 6):
            return False
        for cmd in commands:
            if cmd.startswith("+"):
                parts = cmd.split()
                if len(parts) != 2:
                    return False
                try:
                    number = int(parts[1])
                    if abs(number) > 10 ** 9:
                        return False
                except ValueError:
                    return False
            elif cmd != "-":
                return False
        return True

    def get_results(self):
        """
        Возвращает результаты обработки команд.

        :return: Список результатов.
        """
        return self.results

    @staticmethod
    def write_results(output_path, results):
        """
        Записывает результаты в файл.

        :param output_path: Путь к выходному файлу.
        :param results: Список результатов.
        """
        data = "\n".join(map(str, results))
        IOHandler.write_file(output_path, data)
