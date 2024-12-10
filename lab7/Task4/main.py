# Lab7/Task4/main.py

"""Основной скрипт для нахождения длины LCS двух последовательностей."""

import os
from lab7.Task4.src.LCSFinder import LCSFinder
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
    A = list(map(int, lines[1].strip().split()))
    m = int(lines[2].strip())
    B = list(map(int, lines[3].strip().split()))

    # Проверка данных, если необходимо
    # Предполагается, что они корректны
    result = LCSFinder.longest_common_subsequence(A, B)

    IOHandler.write_file(output_path, str(result))
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == "__main__":
    main()
