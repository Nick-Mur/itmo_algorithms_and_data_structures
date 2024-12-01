import os
from Lab3.utils.IOHandler import IOHandler
from Lab3.Task1.src.Sorter import Sorter
from Lab3.utils.consts import *
from Lab3.utils.decorate import *


@measure_time_and_memory
def main():
    """
    Основная функция для выполнения сортировок и записи результатов.
    """
    # Определение путей к файлам
    current_dir = os.path.dirname(os.path.abspath(__file__))
    txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
    input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
    output_quick_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output_quick.txt')
    output_randomized_quick_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output_randomized_quick.txt')
    output_randomized_p3_quick_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output_randomized_p3_quick.txt')
    output_merge_sort_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output_merge_sort.txt')

    # Чтение входных данных
    arr = IOHandler.read_list(input_path)

    # Выполнение сортировок
    sorter = Sorter()
    sorted_results = sorter.perform_sorting(arr)

    # Запись результатов
    IOHandler.write_list(output_quick_path, sorted_results['simple_quick_sort'])
    IOHandler.write_list(output_randomized_quick_path, sorted_results['randomized_quick_sort'])
    IOHandler.write_list(output_randomized_p3_quick_path, sorted_results['randomized_quick_sort_partition3'])
    IOHandler.write_list(output_merge_sort_path, sorted_results['merge_sort'])


if __name__ == '__main__':
    main()
