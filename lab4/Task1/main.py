# Task1/main.py

"""Основной скрипт для запуска обработки стека."""

import os
from lab4.Task1.src.StackProcessor import StackProcessor
from lab4.utils.consts import *
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Основная функция для запуска обработки команд стека."""
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Создание экземпляра обработчика стека
    processor = StackProcessor()

    # Чтение и валидация команд
    commands = processor.read_commands(input_path)
    if not processor.validate_commands(commands):
        print("Введите корректные данные")
        return

    # Обработка команд
    processor.process_commands(commands)

    # Запись результатов
    processor.write_results(output_path, processor.get_results())
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
