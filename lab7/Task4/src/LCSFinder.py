"""Модуль для вычисления длины наибольшей общей подпоследовательности (LCS) двух последовательностей."""


class LCSFinder:
    """
    Класс для нахождения длины наибольшей общей подпоследовательности (LCS).
    """

    @staticmethod
    def longest_common_subsequence(A, B):
        """
        Вычисляет длину LCS для последовательностей A и B.

        :param A: Первая последовательность (список чисел).
        :param B: Вторая последовательность (список чисел).
        :return: Длина LCS.
        """
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
