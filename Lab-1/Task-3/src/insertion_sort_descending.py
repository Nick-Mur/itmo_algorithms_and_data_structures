# insertion_sort_descending.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output


def insertion_sort_descending(arr):
    """
    Функция сортировки массива методом вставки по убыванию.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по убыванию список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые меньше key, на одну позицию вперед
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    _, massive = read_input()
    array = insertion_sort_descending(list(map(int, massive.split())))
    write_output(' '.join(map(str, array)))
