"""Модуль для вычисления длины наибольшей общей подпоследовательности для трёх последовательностей."""

class LCS3Finder:
    """
    Класс для нахождения длины LCS для трёх последовательностей.
    """

    @staticmethod
    def longest_common_subsequence_3(a, b, c):
        """
        Вычисляет длину LCS для трёх последовательностей a, b и c.

        :param a, b, c: Списки чисел.
        :return: Длина LCS для трёх последовательностей.
        """
        n, m, l = len(a), len(b), len(c)
        dp = [[[0]*(l+1) for _ in range(m+1)] for __ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(1, l+1):
                    if a[i-1] == b[j-1] == c[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

        return dp[n][m][l]
