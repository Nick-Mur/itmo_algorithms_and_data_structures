"""Модуль для проверки скобок в строке."""

from lab4.utils.IOHandler import IOHandler


class BracketChecker:
    """Класс для проверки правильности скобок в строке."""

    def __init__(self):
        """Инициализация сопоставления скобок."""
        self.bracket_pairs = {')': '(', ']': '[', '}': '{'}

    def check_brackets(self, data):
        """
        Проверяет строку на корректность расстановки скобок.

        :param data: Строка для проверки.
        :return: "Success" или индекс первой ошибки.
        """
        stack = []
        for index, char in enumerate(data, start=1):
            if char in "([{":
                stack.append((char, index))
            elif char in ")]}":
                if not stack or stack[-1][0] != self.bracket_pairs[char]:
                    return str(index)
                stack.pop()

        if stack:
            # Возвращаем позицию первой незакрытой открывающей скобки
            return str(stack[0][1])

        return "Success"

    @staticmethod
    def read_data(input_path):
        """
        Считывает данные из входного файла.

        :param input_path: Путь к входному файлу.
        :return: Строка с данными.
        """
        lines = IOHandler.read_file(input_path)
        return lines[0].strip()

    @staticmethod
    def write_result(output_path, result):
        """
        Записывает результат в выходной файл.

        :param output_path: Путь к выходному файлу.
        :param result: Результат проверки.
        """
        IOHandler.write_file(output_path, result)
