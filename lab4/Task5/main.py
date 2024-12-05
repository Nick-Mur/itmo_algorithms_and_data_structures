# Task5/main.py

"""Основной скрипт для работы со стеком MaxStack."""

import os
from lab4.Task5.src.MaxStack import MaxStack
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

    # Создание экземпляра стека
    max_stack = MaxStack()

    # Чтение и валидация команд
    n, commands = max_stack.read_commands(input_path)
    if not max_stack.validate_commands(n, commands):
        print("Введите корректные данные")
        return

    # Обработка команд
    output = []
    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            max_stack.push(int(value))
        elif command == "pop":
            max_stack.pop()
        elif command == "max":
            max_value = max_stack.max()
            output.append(str(max_value) if max_value is not None else "None")

    # Запись результатов
    max_stack.write_results(output_path, output)
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
