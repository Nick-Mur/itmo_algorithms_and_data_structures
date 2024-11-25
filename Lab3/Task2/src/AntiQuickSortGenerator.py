"""
Модуль для генерации перестановки, на которой QuickSort выполняет максимальное количество сравнений.
"""

class AntiQuickSortGenerator:
    """
    Класс для генерации требуемой перестановки.
    """

    @staticmethod
    def generate(n: int) -> list:
        """
        Генерирует перестановку для заданного n, на которой QuickSort выполнит максимальное количество сравнений.

        :param n: Размер перестановки.
        :return: Список, представляющий перестановку.
        """
        if n == 0:
            return []

        res = list(range(1, n + 1))

        for i in range(2, n):
            res[i], res[i // 2] = res[i // 2], res[i]

        return res
