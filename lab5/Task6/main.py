# Lab5/Task6/main.py

"""Основной скрипт для обработки приоритетной очереди."""

import os
from lab5.Task6.src.PriorityQueueProcessor import PriorityQueueProcessor
from lab5.utils.IOHandler import IOHandler
from lab5.utils.consts import *
from lab5.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    n = int(lines[0])
    operations = lines[1:]

    # Валидация данных при необходимости
    processor = PriorityQueueProcessor()
    results = processor.process_operations(operations)

    IOHandler.write_file(output_path, "\n".join(results))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
