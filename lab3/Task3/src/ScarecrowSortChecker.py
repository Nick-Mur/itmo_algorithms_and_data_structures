"""
Модуль для проверки возможности сортировки массива методом "Сортировка пугалом".
"""

from typing import List

class ScarecrowSortChecker:
    """
    Класс для проверки возможности сортировки массива методом "Сортировка пугалом".
    """

    @staticmethod
    def can_sort(n: int, k: int, arr: List[int]) -> bool:
        """
        Определяет, можно ли отсортировать массив по неубыванию, используя
        метод "Сортировка пугалом", где можно менять местами элементы на расстоянии k.

        :param n: Количество матрёшек.
        :param k: Размах рук (расстояние для обмена).
        :param arr: Список размеров матрёшек.
        :return: True, если сортировка возможна, иначе False.
        :raises ValueError: Если длина массива не равна n.
        """
        if len(arr) != n:
            raise ValueError(f"Ожидалась длина массива {n}, но получено {len(arr)}.")

        # Создаём список групп, где каждая группа соответствует позиции по модулю k
        groups = [[] for _ in range(k)]
        for index in range(n):
            groups[index % k].append(arr[index])

        # Сортируем каждую группу по неубыванию
        for group in groups:
            group.sort()

        # Сортированный массив для сравнения
        sorted_arr = sorted(arr)

        # Проверяем, можно ли собрать отсортированный массив из отсортированных групп
        for index in range(n):
            group_index = index % k
            element_index = index // k
            if element_index >= len(groups[group_index]):
                # Это условие обычно не должно возникать, но добавляем для безопасности
                return False
            actual_value = groups[group_index][element_index]
            expected_value = sorted_arr[index]
            if actual_value != expected_value:
                return False
        return True
