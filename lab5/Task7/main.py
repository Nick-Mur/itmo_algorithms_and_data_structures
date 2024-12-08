# Lab5/Task7/main.py

"""Основной скрипт для пирамидальной сортировки."""

import os
from lab5.Task7.src.HeapSorter import HeapSorter
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
    n_str, m_str = lines[0].strip(), lines[1].strip()
    n = int(n_str)
    m = list(map(int, m_str.split()))

    # Проверка входных данных при необходимости
    sorter = HeapSorter()
    sorter.heapsort(m)
    m.reverse()  # переворачиваем для убывающего порядка

    IOHandler.write_file(output_path, " ".join(map(str, m)))
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
