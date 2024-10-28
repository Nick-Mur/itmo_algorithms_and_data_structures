import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import *


def insertion_sort(arr):
    """
    Функция для сортировки массива методом вставки.

    Алгоритм сортирует элементы, перенося каждый новый элемент в отсортированную часть массива.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по возрастанию список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    _, massive = read_input()
    array = insertion_sort(list(map(int, massive.split())))
    write_output(' '.join(map(str, array)))
