"""
Модуль с тестами для PointSegmentsCounter.
"""

import unittest
from lab3.Task4.src.PointSegmentsCounter import PointSegmentsCounter

class TestPointSegmentsCounter(unittest.TestCase):
    """
    Класс для тестирования PointSegmentsCounter.
    """

    def test_example1(self):
        s = 2
        p = 3
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected = [1, 0, 0]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_example2(self):
        s = 1
        p = 3
        segments = [(-10, 10)]
        points = [-10, 0, 10]
        expected = [1, 1, 1]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_example3(self):
        s = 3
        p = 3
        segments = [(2, 3), (2, 5), (2, 7)]
        points = [1, 2, 8]
        expected = [0, 3, 0]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_single_segment_contains_all_points(self):
        s = 1
        p = 5
        segments = [(0, 100)]
        points = [0, 50, 100, -10, 110]
        expected = [1, 1, 1, 0, 0]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_no_segments(self):
        s = 0
        p = 3
        segments = []
        points = [1, 2, 3]
        expected = [0, 0, 0]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_overlapping_segments(self):
        s = 4
        p = 5
        segments = [(1, 4), (2, 5), (3, 6), (4, 7)]
        points = [2, 3, 4, 5, 6]
        expected = [2, 3, 4, 3, 2]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_large_input(self):
        s = 50000
        p = 50000
        segments = [(i, i + 100) for i in range(0, 50000)]
        points = [i for i in range(50000, 100000)]
        # Каждый пункт x от 50000 до 50099 включительно содержится в 50100 - x отрезках
        # Для x >=50100, нет отрезков, содержащих x
        expected = []
        for x in points:
            if x < 100:
                expected.append(x)
            elif x <= 50099:
                expected.append(50100 - x)
            else:
                expected.append(0)
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_points_on_segment_boundaries(self):
        s = 3
        p = 6
        segments = [(1, 5), (5, 10), (10, 15)]
        points = [1, 5, 10, 0, 16, 7]
        expected = [1, 2, 2, 0, 0, 1]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

    def test_negative_coordinates(self):
        segments = [(-10, -5), (-7, -3), (-6, -2)]
        points = [-10, -6, -4, 0]
        expected = [1, 3, 2, 0]
        result = PointSegmentsCounter.count_segments(segments, points)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
