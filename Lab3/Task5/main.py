"""
Основной скрипт для задачи 5: Вычисление H-индекса.
"""

import os
from Lab3.utils.IOHandler import IOHandler
from Lab3.Task5.src.HIndexCalculator import HIndexCalculator

def main():
    """
    Основная функция для чтения входных данных, вычисления H-индекса
    и записи результата в выходной файл.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, 'txtf')
    input_path = IOHandler.get_path(txtf_dir, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, 'output.txt')

    # Чтение входных данных
    try:
        citations = IOHandler.read_input_h_index(input_path)
    except ValueError as ve:
        # Если входные данные некорректны, записываем "0"
        IOHandler.write_output_h_index(output_path, 0)
        return

    # Вычисление H-индекса
    h_index = HIndexCalculator.calculate_h_index(citations)

    # Запись результата
    IOHandler.write_output_h_index(output_path, h_index)

if __name__ == '__main__':
    main()
