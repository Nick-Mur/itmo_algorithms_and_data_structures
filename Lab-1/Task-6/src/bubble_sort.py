# bubble_sort.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output


def bubble_sort(arr):
    """
    Функция пузырьковой сортировки.

    Алгоритм многократно сравнивает соседние элементы и меняет их местами, если они не упорядочены.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по возрастанию список.
    """
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    _, massive = read_input()
    array = bubble_sort(list(map(int, massive.split())))
    write_output(' '.join(map(str, array)))
