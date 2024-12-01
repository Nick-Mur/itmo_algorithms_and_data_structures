"""
Основной скрипт для задачи 4: Точки и отрезки.
"""

import os
from Lab3.utils.IOHandler import IOHandler
from Lab3.Task4.src.PointSegmentsCounter import PointSegmentsCounter
from Lab3.utils.consts import *
from Lab3.utils.decorate import *


@measure_time_and_memory
def main():
    """
    Основная функция для подсчёта количества отрезков, содержащих каждую точку,
    и записи результатов в выходной файл.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

    # Чтение входных данных
    try:
        _, _, segments, points = IOHandler.read_input_point_segments(input_path)
    except ValueError as ve:
        # Если входные данные некорректны, записываем "0" для всех точек
        IOHandler.write_output_point_segments(output_path, [0] * len(points) if 'points' in locals() else [])
        return

    # Подсчёт количества отрезков для каждой точки
    counts = PointSegmentsCounter.count_segments(segments, points)

    # Запись результата
    IOHandler.write_output_point_segments(output_path, counts)

if __name__ == '__main__':
    main()
