# Lab5/Task2/main.py

"""Основной скрипт для вычисления высоты дерева."""

import os
from lab5.Task2.src.TreeHeightCalculator import TreeHeightCalculator
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import *
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    # Предполагаемый формат: первая строка — n, вторая строка — список родителей
    n = int(lines[0].strip())
    parents = list(map(int, lines[1].split()))

    # Проверка корректности входных данных
    # Можно добавить проверки по условию, если требуется
    calculator = TreeHeightCalculator()
    result = calculator.tree_height(n, parents)

    IOHandler.write_file(output_path, str(result))
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
