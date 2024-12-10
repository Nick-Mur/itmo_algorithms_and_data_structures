"""Основной скрипт для проверки совпадения строки с шаблоном."""

import os
from lab7.Task7.src.PatternMatcher import PatternMatcher
from lab7.utils.IOHandler import IOHandler
from lab7.utils.consts import *
from lab7.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    pattern = lines[0].strip() if len(lines) > 0 else ""
    string = lines[1].strip() if len(lines) > 1 else ""

    if len(pattern) <= 10_000 and len(string) <= 10_000:
        result = PatternMatcher.matches_pattern(pattern, string)
        IOHandler.write_file(output_path, result)
        print("Обработка завершена. Результат записан в output.txt")
    else:
        print("Введите корректные данные")


if __name__ == "__main__":
    main()
