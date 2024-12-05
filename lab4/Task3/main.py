# Task3/main.py

"""Основной скрипт для проверки скобочных последовательностей."""

import os
from lab4.Task3.src.BracketSequenceChecker import BracketSequenceChecker
from lab4.utils.consts import *
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Основная функция для запуска проверки скобочных последовательностей."""
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Создание экземпляра проверяющего
    checker = BracketSequenceChecker()

    # Чтение и валидация входных данных
    n, sequences = checker.read_sequences(input_path)
    if not checker.validate_input(n, sequences):
        print("Введите корректные данные")
        return

    # Обработка последовательностей
    results = checker.process_sequences(sequences)

    # Запись результатов
    checker.write_results(output_path, results)
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
