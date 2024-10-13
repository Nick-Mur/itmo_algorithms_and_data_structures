def selection_sort(arr):
    """
    Функция сортировки выбором.

    Алгоритм последовательно находит минимальный элемент и ставит его на нужное место.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по возрастанию список.
    """
    for i in range(len(arr)):
        min_idx = i
        # Поиск минимального элемента в оставшейся части массива
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами минимальный элемент и текущий элемент
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = selection_sort(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
