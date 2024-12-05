# Task8/src/PostfixEvaluator.py

"""Модуль для вычисления выражений в постфиксной записи."""

from lab4.utils.IOHandler import IOHandler
from lab4.utils.consts import *


class PostfixEvaluator:
    """Класс для вычисления выражений в постфиксной записи."""

    def __init__(self):
        """Инициализация класса."""
        self.bracket_limit = 2 ** 31

    def evaluate_postfix(self, expression):
        """
        Вычисляет значение выражения в постфиксной записи.

        :param expression: Список строк, представляющих постфиксное выражение.
        :return: Результат вычисления.
        :raises ValueError: Если найдено число, выходящее за пределы |2^31|,
                            или если обнаружен неизвестный оператор.
        :raises IndexError: Если выражение некорректно (например, недостаточно операндов).
        """
        stack = []  # Инициализируем стек для промежуточных значений

        for token in expression:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                # Если токен - число, помещаем его в стек
                num = int(token)
                if abs(num) >= self.bracket_limit:
                    raise ValueError("Найдено число, выходящее за пределы |2^31|")
                stack.append(num)
            else:
                # Если токен - оператор, выполняем соответствующую операцию
                if len(stack) < 2:
                    raise IndexError("Недостаточно операндов для выполнения операции")
                b = stack.pop()  # Второй операнд
                a = stack.pop()  # Первый операнд

                # Выполняем операцию в зависимости от оператора
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:
                    raise ValueError(f"Неизвестный оператор: {token}")

                # Проверяем, не превышает ли промежуточный результат предел
                if abs(result) >= self.bracket_limit:
                    raise ValueError("Промежуточный результат превышает предел |2^31|")
                stack.append(result)

        if len(stack) != 1:
            raise IndexError("Некорректное выражение")

        return stack.pop()

    @staticmethod
    def read_expression(input_path):
        """
        Считывает выражение из входного файла.

        :param input_path: Путь к входному файлу.
        :return: Кортеж из числа элементов и списка элементов выражения.
        """
        lines = IOHandler.read_file(input_path)
        if not lines:
            raise ValueError("Входной файл пуст")
        n = int(lines[0].strip())
        expr = lines[1].strip().split()
        return n, expr

    @staticmethod
    def validate_input(n, expr):
        """
        Валидирует входные данные.

        :param n: Количество элементов в выражении.
        :param expr: Список элементов выражения.
        :return: True, если данные валидны, иначе False.
        """
        if not (1 <= n <= 10 ** 6):
            return False
        if len(expr) != n:
            return False
        for token in expr:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                num = int(token)
                if abs(num) >= 2 ** 31:
                    return False
            elif token not in ('+', '-', '*'):
                return False
        return True

    @staticmethod
    def write_result(output_path, result):
        """
        Записывает результат в выходной файл.

        :param output_path: Путь к выходному файлу.
        :param result: Результат вычисления.
        """
        IOHandler.write_file(output_path, str(result))
