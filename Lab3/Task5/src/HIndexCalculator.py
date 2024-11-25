"""
Модуль для решения задачи 5: Вычисление H-индекса.
"""

from typing import List

class HIndexCalculator:
    """
    Класс для вычисления H-индекса.
    """

    @staticmethod
    def calculate_h_index(citations: List[int]) -> int:
        """
        Вычисляет H-индекс по списку цитирований.

        :param citations: Список чисел, представляющих количество цитирований каждой публикации.
        :return: H-индекс.
        """
        # Сортируем цитирования по убыванию
        sorted_citations = sorted(citations, reverse=True)

        h_index = 0
        for i, citation in enumerate(sorted_citations, start=1):
            if citation >= i:
                h_index = i
            else:
                break

        return h_index
