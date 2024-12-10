# Lab2/Task1/main.py

"""Основной скрипт для сортировки массива методом слияния."""

import os
from lab2.Task1.src.MergeSorter import MergeSorter
from lab2.utils.IOHandler import IOHandler
from lab2.utils.consts import *
from lab2.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    # Чтение данных
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    array = list(map(int, lines[0].split()))

    # Сортировка
    MergeSorter.merge_sort(array, 0, len(array) - 1)

    # Запись результата
    IOHandler.write_file(output_path, ' '.join(map(str, array)))
    print("Обработка завершена. Результат записан в output.txt")

if __name__ == '__main__':
    main()