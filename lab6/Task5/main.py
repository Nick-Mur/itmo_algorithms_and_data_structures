"""Основной скрипт для обработки результатов выборов."""

import os
from lab6.Task5.src.ElectionsProcessor import ElectionsProcessor
from lab6.utils.IOHandler import IOHandler
from lab6.utils.consts import *
from lab6.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    lines = IOHandler.read_file(input_path)
    data = []
    for line in lines:
        parts = line.strip().split()
        # Предполагается формат: кандидат количество_голосов
        if len(parts) == 2:
            candidate, vote_count = parts
            data.append((candidate, vote_count))

    processor = ElectionsProcessor()
    res = processor.process_elections(data)

    IOHandler.write_file(output_path, "".join(res))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
