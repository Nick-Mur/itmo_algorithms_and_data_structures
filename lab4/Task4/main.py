# Task4/main.py

"""Основной скрипт для проверки скобок в строке."""

import os
from lab4.Task4.src.BracketChecker import BracketChecker
from lab4.utils.consts import *
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Основная функция для запуска проверки скобок."""
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Создание экземпляра проверяющего
    checker = BracketChecker()

    # Чтение данных
    data = checker.read_data(input_path)

    # Проверка скобок
    result = checker.check_brackets(data)

    # Запись результата
    checker.write_result(output_path, result)
    print(f"Результат проверки: {result}")
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
