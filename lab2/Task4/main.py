# Lab2/Task4/main.py

import os
import sys
from lab2.Task4.src.BinarySearcher import BinarySearcher
from lab2.utils.IOHandler import IOHandler
from lab2.utils.consts import *
from lab2.utils.decorate import measure_time_and_memory

@measure_time_and_memory
def main():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        txtf_dir = IOHandler.get_path(current_dir, TXT_DIR)
        input_path = IOHandler.get_path(txtf_dir, INPUT_FILES_DIR, 'input.txt')
        output_path = IOHandler.get_path(txtf_dir, OUTPUT_FILES_DIR, 'output.txt')

        lines = IOHandler.read_file(input_path)

        if len(lines) < 4:
            print("Ошибка: Входной файл должен содержать четыре строки: n, массив A, m, массив B.")
            sys.exit(1)

        # Чтение количества элементов в массиве A
        try:
            n = int(lines[0].strip())
        except ValueError:
            print("Ошибка: Первая строка должна содержать одно целое число (n).")
            sys.exit(1)

        # Чтение массива A
        try:
            array_A = list(map(int, lines[1].strip().split()))
            if len(array_A) != n:
                print(f"Ошибка: Количество элементов в массиве A ({len(array_A)}) не совпадает с n ({n}).")
                sys.exit(1)
        except ValueError:
            print("Ошибка: Вторая строка должна содержать n целых чисел, разделённых пробелами.")
            sys.exit(1)

        # Чтение количества целевых чисел m
        try:
            m = int(lines[2].strip())
        except ValueError:
            print("Ошибка: Третья строка должна содержать одно целое число (m).")
            sys.exit(1)

        # Чтение массива B (целевых чисел)
        try:
            array_B = list(map(int, lines[3].strip().split()))
            if len(array_B) != m:
                print(f"Ошибка: Количество элементов в массиве B ({len(array_B)}) не совпадает с m ({m}).")
                sys.exit(1)
        except ValueError:
            print("Ошибка: Четвёртая строка должна содержать m целых чисел, разделённых пробелами.")
            sys.exit(1)

        # Проверка, что массив A отсортирован по возрастанию
        if array_A != sorted(array_A):
            print("Ошибка: Массив A должен быть отсортирован по возрастанию для корректного бинарного поиска.")
            sys.exit(1)

        # Выполнение бинарного поиска для каждого элемента из массива B
        results = BinarySearcher.multi_search(array_A, array_B)

        # Форматирование результатов: индексы разделяются пробелами
        results_str = ' '.join(map(str, results))

        # Запись результатов в output.txt
        IOHandler.write_file(output_path, results_str)
        print("Обработка завершена. Результат записан в output.txt")

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
