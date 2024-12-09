
"""Основной скрипт для проверки чисел на принадлежность ряду Фибоначчи."""

import os
from lab6.Task6.src.FibonacciChecker import FibonacciChecker
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import *
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    # Первая строка — количество чисел, далее сами числа
    n = int(lines[0].strip())
    numbers = list(map(int, lines[1:]))

    checker = FibonacciChecker()
    res = checker.process_fibonacci(numbers)

    IOHandler.write_file(output_path, "".join(res))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
