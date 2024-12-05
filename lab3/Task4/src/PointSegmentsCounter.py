"""
Модуль для решения задачи 4: Точки и отрезки.
"""

from typing import List, Tuple
import bisect

class PointSegmentsCounter:
    """
    Класс для подсчёта количества отрезков, содержащих каждую точку.
    """

    @staticmethod
    def count_segments(segments: List[Tuple[int, int]], points: List[int]) -> List[int]:
        """
        Подсчитывает для каждой точки количество отрезков, содержащих её.

        :param segments: Список кортежей (a_i, b_i), определяющих отрезки.
        :param points: Список координат точек.
        :return: Список количеств отрезков, содержащих каждую точку.
        """
        # Разделяем начальные и конечные точки отрезков
        starts = sorted(a for a, b in segments)
        ends = sorted(b for a, b in segments)

        result = []
        for x in points:
            # Количество отрезков, начинающихся не позже x
            count_starts = bisect.bisect_right(starts, x)
            # Количество отрезков, заканчивающихся до x-1 (т.е., b_i < x)
            count_ends = bisect.bisect_left(ends, x)
            # Количество отрезков, содержащих x
            count = count_starts - count_ends
            result.append(count)

        return result
