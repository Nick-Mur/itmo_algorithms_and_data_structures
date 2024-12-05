"""
Основной скрипт для задачи 3: Сортировка пугалом.
"""

import os
from lab3.utils.IOHandler import IOHandler
from lab3.Task3.src.ScarecrowSortChecker import ScarecrowSortChecker
from lab3.utils.consts import *
from lab3.utils.decorate import *


@measure_time_and_memory
def main():
    """
    Основная функция для проверки возможности сортировки массива методом "Сортировка пугалом"
    и записи результата в выходной файл.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Чтение входных данных
    try:
        n, k, arr = IOHandler.read_input_scarecrow_sort(input_path)
    except ValueError as ve:
        # Если входные данные некорректны, записываем "НЕТ"
        IOHandler.write_result(output_path, "НЕТ")
        return

    # Проверка возможности сортировки
    try:
        is_sortable = ScarecrowSortChecker.can_sort(n, k, arr)
    except ValueError:
        # Если произошла ошибка в проверке, записываем "НЕТ"
        IOHandler.write_result(output_path, "НЕТ")
        return

    # Запись результата
    result = "ДА" if is_sortable else "НЕТ"
    IOHandler.write_result(output_path, result)

if __name__ == '__main__':
    main()
