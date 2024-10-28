# insertion_sort_with_indices.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output


def insertion_sort(list_arr):
    """
    Функция сортировки вставками, которая отслеживает перемещения элементов.
    Возвращает индексы конечных позиций элементов и отсортированный массив.

    :param list_arr: Список целых чисел для сортировки.
    :return: Список индексов конечных позиций и отсортированный список.
    """
    index_result = [1]  # Начинаем с первого индекса, так как первый элемент уже на месте
    for i in range(1, len(list_arr)):
        for j in range(i - 1, -1, -1):
            if list_arr[i] < list_arr[j]:
                # Меняем местами элементы и обновляем их позиции
                list_arr[i], list_arr[j] = list_arr[j], list_arr[i]
                i, j = j, i
        index_result.append(i + 1)  # Добавляем индекс, начиная с 1
    return index_result, list_arr


if __name__ == '__main__':
    _, massive = read_input()
    indexes, array = insertion_sort(list(map(int, massive.split())))
    write_output(' '.join(map(str, indexes)), ' '.join(map(str, array)))
