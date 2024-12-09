import unittest
from lab6.Task6.src.FibonacciChecker import FibonacciChecker

class TestFibonacciChecker(unittest.TestCase):

    def setUp(self):
        self.checker = FibonacciChecker()

    def test_process_fibonacci(self):
        numbers = [0, 1, 1, 4, 5, 10, 11, 8]
        # 0 (Fibo), 1(Fibo), 1(Fibo),4(!),5(Fibo),10(!),11(!),8(Fibo)
        # Ожидаем: Yes, Yes, Yes, No, Yes, No, No, Yes
        result = self.checker.process_fibonacci(numbers)
        self.assertEqual(result, ["Yes\n", "Yes\n", "Yes\n", "No\n", "Yes\n", "No\n", "No\n", "Yes\n"])


if __name__ == '__main__':
    unittest.main()
