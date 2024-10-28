# merge_sort.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output

def merge(array, left, middle, right):
    """
    Функция слияния двух отсортированных подмассивов в один.

    :param array: исходный массив
    :param left: начальный индекс первого подмассива
    :param middle: разделительный индекс (конец первого подмассива)
    :param right: конечный индекс второго подмассива
    :raises ValueError: если индексы некорректны
    """
    if left < 0 or right >= len(array) or left > right:
        raise ValueError("Некорректные индексы для слияния.")

    left_subarray = array[left:middle + 1] + [float('inf')]
    right_subarray = array[middle + 1:right + 1] + [float('inf')]

    i = j = 0
    for k in range(left, right + 1):
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1

def merge_sort(array, left, right):
    """
    Функция рекурсивной сортировки массива методом слияния.

    :param array: исходный массив
    :param left: начальный индекс массива
    :param right: конечный индекс массива
    :raises ValueError: если индексы некорректны
    """
    if left < 0 or right >= len(array):
        raise ValueError("Некорректные индексы для сортировки.")

    if left >= right:  # Если массив пустой или отсортирован (1 элемент)
        return

    middle = (left + right) // 2
    merge_sort(array, left, middle)
    merge_sort(array, middle + 1, right)
    merge(array, left, middle, right)

if __name__ == '__main__':
    _, massive = read_input(task=1)
    array = list(map(int, massive.split()))
    merge_sort(array, 0, len(array) - 1)
    write_output(1, ' '.join(map(str, array)))
