"""
Модуль для решения задачи 6: Сумма выбранных произведений.
"""

from typing import List

class ProductSumCalculator:
    """
    Класс для вычисления суммы выбранных произведений матриц A и B.
    """

    @staticmethod
    def calculate_sum_of_selected_products(A: List[int], B: List[int]) -> int:
        """
        Вычисляет сумму самого маленького произведения и одиннадцатого по величине произведения матриц A и B.
        Если количество произведений меньше 11, возвращает сумму всех произведений.

        :param A: Список целых чисел, представляющих матрицу A.
        :param B: Список целых чисел, представляющих матрицу B.
        :return: Сумма выбранных произведений.
        """
        if not A or not B:
            return 0

        # Вычисляем все произведения элементов из A и B
        products = [a * b for a in A for b in B]

        # Сортируем произведения по возрастанию
        products.sort()

        # Определяем сумму выбранных произведений
        if len(products) > 10:
            return products[0] + products[10]
        else:
            return sum(products)
