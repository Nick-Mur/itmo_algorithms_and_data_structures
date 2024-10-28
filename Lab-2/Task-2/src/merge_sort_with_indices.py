# merge_sort_with_indices.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output


def merge_with_indices(array, left, middle, right):
    """
    Слияние с выводом индексов подмассивов и их значений.

    :param array: исходный массив
    :param left: начальный индекс первого подмассива
    :param middle: разделительный индекс (конец первого подмассива)
    :param right: конечный индекс второго подмассива
    """
    left_subarray = array[left:middle + 1] + [float('inf')]
    right_subarray = array[middle + 1:right + 1] + [float('inf')]

    i = j = 0
    print(f"Слияние: индексы {left + 1}-{right + 1}, значения: {array[left]}-{array[right]}")

    for k in range(left, right + 1):
        if left_subarray[i] <= right_subarray[j]:
            array[k] = left_subarray[i]
            i += 1
        else:
            array[k] = right_subarray[j]
            j += 1


def merge_sort_with_indices(array, left, right):
    """
    Рекурсивная сортировка с выводом индексов.

    :param array: исходный массив
    :param left: начальный индекс массива
    :param right: конечный индекс массива
    :raises ValueError: если индексы некорректны
    """
    if left < 0 or right >= len(array):
        raise ValueError("Некорректные индексы для сортировки.")

    if left >= right:
        # Если массив пустой или left больше или равен right, завершить работу
        return

    middle = (left + right) // 2
    merge_sort_with_indices(array, left, middle)
    merge_sort_with_indices(array, middle + 1, right)
    merge_with_indices(array, left, middle, right)


if __name__ == '__main__':
    _, massive = read_input(task=2)
    array = list(map(int, massive.split()))
    merge_sort_with_indices(array, 0, len(array) - 1)
    write_output(2, ' '.join(list(map(str, array))))
