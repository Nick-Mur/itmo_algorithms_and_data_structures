# merge_sort_and_count.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output

def merge_and_count(array, temp_array, left, middle, right):
    """
    Слияние двух подмассивов с подсчетом инверсий.

    :param array: исходный массив
    :param temp_array: временный массив
    :param left: начальный индекс
    :param middle: разделительный индекс
    :param right: конечный индекс
    :return: количество инверсий
    """
    i = left
    j = middle + 1
    k = left
    inv_count = 0

    while i <= middle and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            temp_array[k] = array[j]
            inv_count += (middle - i + 1)
            j += 1
        k += 1

    while i <= middle:
        temp_array[k] = array[i]
        i += 1
        k += 1

    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        array[idx] = temp_array[idx]

    return inv_count

def merge_sort_and_count(array, temp_array, left, right):
    """
    Сортировка с подсчетом инверсий.

    :param array: исходный массив
    :param temp_array: временный массив
    :param left: начальный индекс
    :param right: конечный индекс
    :return: количество инверсий
    :raises ValueError: если временный массив слишком мал
    :raises TypeError: если входные данные некорректного типа
    """
    if not isinstance(array, list) or not isinstance(temp_array, list):
        raise TypeError("Ожидается массив (list).")

    if len(temp_array) < len(array):
        raise ValueError("Временный массив слишком мал для сортировки.")

    inv_count = 0
    if left < right:
        middle = (left + right) // 2

        inv_count += merge_sort_and_count(array, temp_array, left, middle)
        inv_count += merge_sort_and_count(array, temp_array, middle + 1, right)
        inv_count += merge_and_count(array, temp_array, left, middle, right)

    return inv_count

if __name__ == '__main__':
    _, massive = read_input()
    array = list(map(int, massive.split()))
    temp_array = [0] * len(array)
    inv_count = merge_sort_and_count(array, temp_array, 0, len(array) - 1)
    write_output(str(inv_count))
