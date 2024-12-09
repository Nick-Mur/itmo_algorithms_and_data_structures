import unittest
from lab6.Task8.src.HashSolver import HashSolver

class TestHashSolver(unittest.TestCase):

    def setUp(self):
        self.solver = HashSolver()

    def test_solve_hash(self):
        # Допустим, что входные данные такие, что результат должен быть "3 1 1"
        data = [
            [3, 0, 1, 1],  # N=3, X=0, A=1, B=1
            [0,0,0,0]      # AC=0, BC=0, AD=0, BD=0 (например)
        ]
        # При этом, после 3 итераций, ожидаем X=3, A=1, B=1
        result = self.solver.solve_hash(data)
        self.assertEqual(result, "3 1 1")


if __name__ == '__main__':
    unittest.main()
