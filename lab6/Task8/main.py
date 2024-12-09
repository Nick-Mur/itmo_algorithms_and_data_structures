"""Основной скрипт для решения хеш-задачи."""

import os
from lab6.Task8.src.HashSolver import HashSolver
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
    # Первая строка: N X A B
    # Вторая строка: AC BC AD BD
    first_line = list(map(int, lines[0].split()))
    second_line = list(map(int, lines[1].split()))

    data = [first_line, second_line]

    solver = HashSolver()
    res = solver.solve_hash(data)

    IOHandler.write_file(output_path, res)
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
