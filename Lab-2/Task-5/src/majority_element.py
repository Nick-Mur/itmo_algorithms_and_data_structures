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

    if array.count(candidate) > len(array) // 2:
        return candidate
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = list(map(int, massive.split()))
    result = majority_element(array)
    with open('output.txt', 'w') as f:
        print(result if result else "Нет элемента большинства", file=f)
