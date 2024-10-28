# majority_element.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from utils import read_input, write_output

def majority_element(array):
    """
    Нахождение элемента, встречающегося более чем n/2 раз.

    :param array: массив элементов
    :return: элемент или None, если нет большинства
    :raises TypeError: если передан некорректный тип данных
    """
    if not isinstance(array, list):
        raise TypeError("Ожидается массив (list).")

    candidate = None
    count = 0

    for num in array:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    if candidate is not None and array.count(candidate) > len(array) // 2:
        return candidate
    return None

if __name__ == '__main__':
    _, massive = read_input(task=5)
    array = list(map(int, massive.split()))
    result = majority_element(array)
    output = str(result) if result is not None else "Нет элемента большинства"
    write_output(5, output)
