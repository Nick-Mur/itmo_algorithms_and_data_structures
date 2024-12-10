"""Основной скрипт для нахождения наибольшей возрастающей подпоследовательности (LIS)."""

import os
from lab7.Task6.src.LISFinder import LISFinder
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
    sequence = list(map(int, lines[1].strip().split()))

    lis_length, lis_sequence = LISFinder.find_lis(sequence)

    IOHandler.write_file(output_path, f"{lis_length}\n" + " ".join(map(str, lis_sequence)))
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
