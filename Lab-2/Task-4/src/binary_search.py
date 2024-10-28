# binary_search.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output

def binary_search(array, target):
    """
    Бинарный поиск элемента в отсортированном массиве.

    :param array: отсортированный массив
    :param target: искомый элемент
    :return: индекс элемента или -1, если не найден
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == '__main__':
    _, massive, target = read_input()
    array = list(map(int, massive.split()))
    result = binary_search(array, int(target))
    write_output(str(result))
