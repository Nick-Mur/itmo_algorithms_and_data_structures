"""
Основной скрипт для задачи 2: Анти-QuickSort.
"""

import os
from Lab3.utils.IOHandler import IOHandler
from Lab3.Task2.src.AntiQuickSortGenerator import AntiQuickSortGenerator
from Lab3.utils.consts import *
from Lab3.utils.decorate import *


@measure_time_and_memory
def main():
    """
    Основная функция для генерации перестановки и записи результата.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Чтение n из входного файла
    n = IOHandler.read_integer(input_path)

    # Генерация перестановки
    permutation = AntiQuickSortGenerator.generate(n)

    # Запись перестановки в выходной файл
    IOHandler.write_list(output_path, permutation)


if __name__ == '__main__':
    main()
