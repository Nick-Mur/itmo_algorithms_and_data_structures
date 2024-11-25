"""
Основной скрипт для задачи 2: Анти-QuickSort.
"""

import os
from Lab3.utils.IOHandler import IOHandler
from Lab3.Task2.src.AntiQuickSortGenerator import AntiQuickSortGenerator


def main():
    """
    Основная функция для генерации перестановки и записи результата.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, 'txtf')
    input_path = IOHandler.get_path(txtf_dir, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, 'output.txt')

    # Чтение n из входного файла
    n = IOHandler.read_integer(input_path)

    # Генерация перестановки
    permutation = AntiQuickSortGenerator.generate(n)

    # Запись перестановки в выходной файл
    IOHandler.write_list(output_path, permutation)


if __name__ == '__main__':
    main()
