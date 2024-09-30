def insertion_sort_with_indexes(arr):
    """
    Функция сортировки вставками, которая также отслеживает перемещения элементов.
    Возвращает индексы исходных элементов массива после сортировки.

    :param arr: Список целых чисел для сортировки.
    :return: Список индексов, который соответствует отсортированным элементам.
    """
    n = len(arr)
    indexes = list(range(n))  # Создаем список индексов от 0 до n-1
    for i in range(1, n):
        key = arr[i]
        key_index = indexes[i]
        j = i - 1
        # Перемещаем элементы, которые больше ключевого, на одну позицию вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            indexes[j + 1] = indexes[j]
            j -= 1
        arr[j + 1] = key
        indexes[j + 1] = key_index  # Вставляем исходный индекс ключевого элемента
    return indexes
