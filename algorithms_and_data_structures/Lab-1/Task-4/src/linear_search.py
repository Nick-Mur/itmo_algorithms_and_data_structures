def linear_search(arr, v):
    """
    Функция для поиска элемента в массиве с использованием линейного поиска.

    Возвращает индексы всех вхождений элемента v в массив arr или -1, если элемент не найден.

    :param arr: Список целых чисел для поиска.
    :param v: Элемент для поиска.
    :return: Список индексов или -1, если элемент не найден.
    """
    result = []
    for i, num in enumerate(arr):
        if num == v:
            result.append(i)
    return result if result else -1
