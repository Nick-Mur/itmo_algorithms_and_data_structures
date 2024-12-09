"""Модуль для проверки корректности скобочных последовательностей."""


from lab4.utils.IOHandler import IOHandler

class BracketSequenceChecker:
    """Класс для проверки правильности скобочных последовательностей."""

    def __init__(self):
        """Инициализация сопоставления скобок."""
        self.matching_brackets = {')': '(', ']': '[', '}': '{'}

    def is_valid_sequence(self, sequence):
        """
        Проверяет, является ли скобочная последовательность правильной.

        :param sequence: Строка со скобочной последовательностью.
        :return: True, если последовательность правильная, иначе False.
        """
        stack = []

        for char in sequence:
            if char in "([{":  # Открывающая скобка
                stack.append(char)
            elif char in ")]}":  # Закрывающая скобка
                if stack and stack[-1] == self.matching_brackets[char]:
                    stack.pop()
                else:
                    return False
        return not stack  # Если стек пустой, последовательность правильная

    def process_sequences(self, sequences):
        """
        Проверяет список скобочных последовательностей.

        :param sequences: Список строк с последовательностями.
        :return: Список результатов ("YES" или "NO").
        """
        results = []
        for seq in sequences:
            seq = seq.strip()
            if self.is_valid_sequence(seq):
                results.append("YES")
            else:
                results.append("NO")
        return results

    @staticmethod
    def read_sequences(input_path):
        """
        Считывает последовательности из входного файла.

        :param input_path: Путь к входному файлу.
        :return: Список последовательностей.
        """
        lines = IOHandler.read_file(input_path)
        n = int(lines[0])
        sequences = lines[1:]
        return n, sequences

    @staticmethod
    def validate_input(n, sequences):
        """
        Валидирует входные данные.

        :param n: Количество последовательностей.
        :param sequences: Список последовательностей.
        :return: True, если данные валидны, иначе False.
        """
        if not (1 <= n <= 500):
            return False
        if len(sequences) != n:
            return False
        for seq in sequences:
            seq = seq.strip()
            if not (1 <= len(seq) <= 10**4):
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
