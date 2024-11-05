import time
import random


def merge(left, right):
    """
    Объединяет два отсортированных списка в один отсортированный список.
    Оптимизация: если последний элемент левого списка меньше или равен первому элементу правого списка,
    просто объединяем списки без дополнительного слияния.

    :param left: отсортированный список
    :param right: отсортированный список
    :return: объединенный отсортированный список
    """
    if left[-1] <= right[0]:
        return left + right

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr):
    """
    Сортирует массив методом сортировки слиянием с оптимизацией на отсортированных подмассивах.

    :param arr: список элементов
    :return: отсортированный список
    :raises TypeError: если передан некорректный тип данных
    """
    if not isinstance(arr, list):
        raise TypeError("Ожидается массив (list).")

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def insertion_sort(arr):
    """
    Сортирует массив методом вставок.

    :param arr: список элементов
    :return: отсортированный список
    :raises TypeError: если передан некорректный тип данных
    """
    if not isinstance(arr, list):
        raise TypeError("Ожидается массив (list).")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def selection_sort(arr):
    """
    Сортирует массив методом выбора.

    :param arr: список элементов
    :return: отсортированный список
    :raises TypeError: если передан некорректный тип данных
    """
    if not isinstance(arr, list):
        raise TypeError("Ожидается массив (list).")

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def measure_time(sort_func, arr):
    """
    Измеряет время выполнения функции сортировки.

    :param sort_func: функция сортировки
    :param arr: список элементов
    :return: время выполнения в секундах
    """
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

if __name__ == '__main__':
    # Поиск порога, где сортировка слиянием становится быстрее
    max_size = 1000  # Максимальный размер массива для тестирования
    threshold_found = False

    for size in range(1, max_size + 1):
        arr = [random.randint(-10 ** 9, 10 ** 9) for _ in range(size)]
        arr_copy1 = arr.copy()
        arr_copy2 = arr.copy()
        arr_copy3 = arr.copy()

        time_merge = measure_time(merge_sort, arr_copy1)
        time_insertion = measure_time(insertion_sort, arr_copy2)
        time_selection = measure_time(selection_sort, arr_copy3)

        print(f"Размер: {size} | Merge Sort: {time_merge:.6f}s | Insertion Sort: {time_insertion:.6f}s | Selection Sort: {time_selection:.6f}s")

        if not threshold_found and time_merge < time_insertion and time_merge < time_selection:
            print(f"Merge Sort быстрее, чем Insertion Sort и Selection Sort при размере массива: {size}")
            threshold_found = True
            break

    if not threshold_found:
        print(f"Порог не найден в диапазоне до {max_size}")
