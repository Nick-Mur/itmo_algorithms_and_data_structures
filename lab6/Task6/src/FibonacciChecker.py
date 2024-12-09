"""Модуль для проверки, является ли число числом Фибоначчи."""

class FibonacciChecker:
    """
    Класс для проверки, является ли число числом Фибоначчи.
    """

    def process_fibonacci(self, numbers):
        """
        Для списка чисел возвращает "Yes" или "No" для каждого,
        в зависимости от того, является ли число числом Фибоначчи.

        :param numbers: Список чисел.
        :return: Список строк "Yes\n" или "No\n".
        """
        results = []
        for num in numbers:
            if self._is_fibonacci(num):
                results.append("Yes\n")
            else:
                results.append("No\n")
        return results

    def _is_fibonacci(self, num):
        """Проверяет, является ли число Фибоначчи."""
        x1 = 5 * (num**2) + 4
        x2 = 5 * (num**2) - 4
        return self._is_perfect_square(x1) or self._is_perfect_square(x2)

    def _is_perfect_square(self, x):
        if x < 0:
            return False
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return True
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return False
