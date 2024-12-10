"""Основной скрипт для вычисления LCS для трёх последовательностей."""

import os
from lab7.Task5.src.LCS3Finder import LCS3Finder
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import *
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)

    n = int(lines[0].strip())
    a = list(map(int, lines[1].strip().split()))
    m = int(lines[2].strip())
    b = list(map(int, lines[3].strip().split()))
    l = int(lines[4].strip())
    c = list(map(int, lines[5].strip().split()))

    result = LCS3Finder.longest_common_subsequence_3(a, b, c)

    IOHandler.write_file(output_path, str(result))
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == "__main__":
    main()
