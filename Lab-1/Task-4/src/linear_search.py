# linear_search.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output


def linear_search(arr, v):
    """
    Функция для поиска элемента в массиве с использованием линейного поиска.

    Возвращает индексы всех вхождений элемента v в массив arr или -1, если элемент не найден.

    :param arr: Список целых чисел для поиска.
    :param v: Элемент для поиска.
    :return: Список индексов или -1, если элемент не найден.
    """
    result = list()
    for i, num in enumerate(arr):
        if num == v:
            result.append(str(i + 1))
    return result if result else '-1'


if __name__ == '__main__':
    lines = read_input()
    massive, v = lines
    result = linear_search(list(map(int, massive.split())), int(v))
    write_output(', '.join(result))
