"""
Модуль с тестами для ProductSumCalculator.
"""

import unittest
from lab3.Task6.src.ProductSumCalculator import ProductSumCalculator

class TestProductSumCalculator(unittest.TestCase):
    """
    Класс для тестирования ProductSumCalculator.
    """

    def test_example_case(self):
        A = [7, 1, 4, 9]
        B = [2, 7, 8, 11]
        # Все произведения: [14, 49, 56, 77, 2, 7, 8, 11, 8, 28, 32, 44, 18, 63, 72, 99]
        # Отсортированные: [2, 7, 8, 8, 11, 14, 18, 28, 32, 44, 49, 56, 63, 72, 77, 99]
        # products[0] = 2, products[10] = 49, сумма = 51
        expected_sum = 51
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_edge_case_all_zero(self):
        A = [0, 0, 0, 0]
        B = [0, 0, 0, 0]
        # Все произведения: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Отсортированные: [0]*16
        # products[0] = 0, products[10] = 0, сумма = 0
        expected_sum = 0
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_single_element(self):
        A = [1]
        B = [1]
        # Все произведения: [1]
        # Отсортированные: [1]
        # len(products) = 1 < 11, сумма = 1
        expected_sum = 1
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_large_elements(self):
        A = [40000, 40000, 40000, 40000]
        B = [40000, 40000, 40000, 40000]
        # Все произведения: 16 * (40000 * 40000) = 16 * 1600000000 = 25600000000
        # Отсортированные: [1600000000]*16
        # products[0] = 1600000000, products[10] = 1600000000, сумма = 3200000000
        expected_sum = 3200000000
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_no_elements_in_A_or_B(self):
        A = []
        B = [1, 2, 3]
        expected_sum = 0
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

        A = [1, 2, 3]
        B = []
        expected_sum = 0
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_less_than_11_products(self):
        A = [1, 2, 3]
        B = [4]
        # Все произведения: [4, 8, 12]
        # Отсортированные: [4, 8, 12]
        # len(products) = 3 < 11, сумма = 4 + 8 + 12 = 24
        expected_sum = 24
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_exactly_11_products(self):
        A = [1, 2, 3]
        B = [1, 2, 3, 4]
        # Все произведения: [1,2,3,4,2,4,6,8,3,6,9,12]
        # Отсортированные: [1,2,2,3,3,4,4,6,6,8,9,12]
        # len(products) = 12 > 10, сумма = 1 + 9 = 10
        expected_sum = 10
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_mixed_positive_and_negative(self):
        A = [-1, 2, -3]
        B = [4, -5]
        # Все произведения: [-4, 5, 8, -10, -12, 15]
        # Отсортированные: [-12, -10, -4, 5, 8, 15]
        # len(products) = 6 < 11, сумма = -12 + (-10) + (-4) + 5 + 8 + 15 = -12 -10 -4 +5 +8 +15 = -26 +28 = 2
        expected_sum = 2
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_duplicate_elements(self):
        A = [2, 2, 2]
        B = [3, 3]
        # Все произведения: [6,6,6,6,6,6]
        # Отсортированные: [6,6,6,6,6,6]
        # len(products) = 6 < 11, сумма = 6*6 = 36
        expected_sum = 36
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

    def test_negative_elements(self):
        A = [-2, -1]
        B = [-3, 4]
        # Все произведения: [6, -8, 3, -4]
        # Отсортированные: [-8, -4, 3, 6]
        # len(products) = 4 < 11, сумма = -8 + (-4) + 3 + 6 = -12 +9 = -3
        expected_sum = -3
        result = ProductSumCalculator.calculate_sum_of_selected_products(A, B)
        self.assertEqual(result, expected_sum)

if __name__ == '__main__':
    unittest.main()
