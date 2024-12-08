# Lab5/Task3/main.py

"""Основной скрипт для обработки сетевых пакетов."""

import os
from lab5.Task3.src.NetworkPacketsProcessor import NetworkPacketsProcessor
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
    if not lines:
        # Если нет пакетов, ничего не выводим
        return

    # Первая строка - buffer_size и количество пакетов
    first_line = lines[0].strip().split()
    if len(first_line) == 1:
        buffer_size = int(first_line[0])
        n = 0
    else:
        buffer_size = int(first_line[0])
        n = int(first_line[1])

    packets = []
    for line in lines[1:]:
        arr, proc = line.strip().split()
        packets.append((int(arr), int(proc)))

    processor = NetworkPacketsProcessor()
    results = processor.network_packets(buffer_size, packets)

    # Преобразуем времена начала обработки в строки, заменяя -1 на строку '-1'
    output_lines = [str(time_start) for time_start in results]
    IOHandler.write_file(output_path, "\n".join(output_lines))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
