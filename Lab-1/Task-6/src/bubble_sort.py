def bubble_sort(arr):
    """
    Функция пузырьковой сортировки.

    Алгоритм многократно сравнивает соседние элементы и меняет их местами, если они не упорядочены.

    :param arr: Список целых чисел для сортировки.
    :return: Отсортированный по возрастанию список.
    """
    n = len(arr)
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    with open('input.txt') as f:
        n, massive = f.readlines()
    array = bubble_sort(list(map(int, massive.split())))
    with open('output.txt', 'w') as f:
        print(' '.join(list(map(str, array))), file=f)
