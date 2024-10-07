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
    with open('input.txt') as f:
        massive, v = f.readlines()
    result = linear_search(massive.split(), v)
    result = ', '.join(result) if isinstance(result, list) else '-1'
    with open('output.txt', 'w') as f:
        print(result, file=f)
