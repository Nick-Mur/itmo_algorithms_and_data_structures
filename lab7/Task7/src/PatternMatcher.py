"""Модуль для проверки совпадения строки с шаблоном, содержащим '?' и '*'. """

class PatternMatcher:
    """
    Класс для проверки совпадения строки с шаблоном.
    Шаблон может содержать:
    - Буквы
    - '?', соответствующий любому одиночному символу
    - '*', соответствующий нулю или более символов
    """

    @staticmethod
    def matches_pattern(pattern: str, string: str) -> str:
        """
        Проверяет, соответствует ли string шаблону pattern.

        :param pattern: Шаблон.
        :param string: Проверяемая строка.
        :return: "YES" если соответствует, иначе "NO".
        """
        n, m = len(pattern), len(string)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True

        # Инициализация для '*'
        for i in range(1, n+1):
            if pattern[i-1] == '*':
                dp[i][0] = dp[i-1][0]
            else:
                break

        for i in range(1, n+1):
            for j in range(1, m+1):
                if pattern[i-1] == string[j-1] or pattern[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return "YES" if dp[n][m] else "NO"
