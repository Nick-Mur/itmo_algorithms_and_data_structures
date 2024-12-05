"""
Основной скрипт для задачи 6: Сумма выбранных произведений.
"""

import os
from lab3.utils.IOHandler import IOHandler
from lab3.Task6.src.ProductSumCalculator import ProductSumCalculator
from lab3.utils.consts import *
from lab3.utils.decorate import *


@measure_time_and_memory
def main():
    """
    Основная функция для чтения входных данных, вычисления суммы выбранных произведений
    и записи результата в выходной файл.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_file_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_file_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Чтение входных данных
    try:
        n, m, A, B = IOHandler.read_input_product_sum(input_file_path)
    except ValueError as ve:
        # Если входные данные некорректны, записываем 0
        IOHandler.write_output_product_sum(output_file_path, 0)
        return

    # Вычисление суммы выбранных произведений
    total_sum = ProductSumCalculator.calculate_sum_of_selected_products(A, B)

    # Запись результата
    IOHandler.write_output_product_sum(output_file_path, total_sum)

if __name__ == '__main__':
    main()
