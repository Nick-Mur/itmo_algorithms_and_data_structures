# Lab7/Task6/src/LISFinder.py

"""Модуль для нахождения наибольшей возрастающей подпоследовательности (LIS)."""

from bisect import bisect_left

class LISFinder:
    """
    Класс для поиска наибольшей возрастающей подпоследовательности.
    """

    @staticmethod
    def find_lis(sequence):
        """
        Находит длину LIS и саму подпоследовательность.

        :param sequence: Список чисел.
        :return: Кортеж (lis_length, lis_sequence)
        """
        n = len(sequence)
        lis = []
        parent = [-1] * n
        indices = []

        for i in range(n):
            pos = bisect_left(lis, sequence[i])
            if pos == len(lis):
                lis.append(sequence[i])
                indices.append(i)
            else:
                lis[pos] = sequence[i]
                indices[pos] = i

            if pos > 0:
                parent[i] = indices[pos - 1]

        lis_length = len(lis)
        lis_sequence = []
        current_index = indices[-1] if indices else -1

        for _ in range(lis_length):
            lis_sequence.append(sequence[current_index])
            current_index = parent[current_index]

        lis_sequence.reverse()
        return lis_length, lis_sequence
