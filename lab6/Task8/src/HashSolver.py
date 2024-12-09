"""Модуль для вычисления хеш-задачи по заданным параметрам."""


class HashSolver:
    """
    Класс для решения задачи с модификацией значений при обнаружении X в хеш-таблице.
    """

    def solve_hash(self, data):
        """
        Принимает данные в формате:
        Первая строка: N, X, A, B
        Вторая строка: AC, BC, AD, BD

        :param data: Список списков чисел [[N,X,A,B],[AC,BC,AD,BD]]
        :return: Строка "X A B" после всех операций.
        """
        N, X, A, B = data[0]
        AC, BC, AD, BD = data[1]

        hash_table = set()

        for _ in range(N):
            if X in hash_table:
                A = (A + AC) % (10 ** 3)
                B = (B + BC) % (10 ** 15)
            else:
                hash_table.add(X)
                A = (A + AD) % (10 ** 3)
                B = (B + BD) % (10 ** 15)

            X = (X * A + B) % (10 ** 15)

        return f"{X} {A} {B}"
