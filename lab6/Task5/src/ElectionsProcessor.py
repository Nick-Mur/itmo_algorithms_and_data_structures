"""Модуль для обработки результатов выборов."""

class ElectionsProcessor:
    """
    Класс для подсчёта голосов кандидатов.
    Принимает список пар (кандидат, количество_голосов).
    Возвращает список строк с результатами, отсортированных по имени кандидата.
    """

    def process_elections(self, data):
        """
        Обрабатывает результаты выборов.

        :param data: Список кортежей (имя_кандидата, количество_голосов).
        :return: Список строк вида "кандидат голосов\n".
        """
        votes = {}
        for candidate, vote_count in data:
            votes[candidate] = votes.get(candidate, 0) + int(vote_count)

        sorted_candidates = sorted(votes.items())
        res = [f"{candidate} {count}\n" for candidate, count in sorted_candidates]
        return res
