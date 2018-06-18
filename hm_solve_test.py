import unittest
import numpy as np

from hm_table import HMTable
from hm_table_solving import solve_hm_table


class SolveHMTableTest(unittest.TestCase):

    def test_solve_1(self):
        spending_matrix = [
            [3, 4, 2, 8, 1, 7, 3],
            [2, 3, 13, 9, 1, 6, 2],
            [12, 4, 12, 5, 3, 1, 4],
            [5, 6, 1, 7, 11, 8, 6],
            [11, 4, 10, 10, 5, 13, 7],
            [9, 6, 11, 12, 7, 1, 2],
            [2, 4, 8, 5, 9, 3, 10]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0]
        ]
        expected_function_value = 16

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_2(self):
        spending_matrix = [
            [6, 2, 15, 2, 4, 9, 5],
            [12, 11, 1, 13, 8, 11, 13],
            [3, 2, 12, 9, 10, 14, 1],
            [7, 1, 3, 4, 5, 6, 8],
            [8, 9, 14, 3, 11, 18, 12],
            [1, 7, 5, 6, 15, 16, 2],
            [13, 10, 4, 7, 10, 16, 17]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        expected_function_value = 24

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_3(self):
        spending_matrix = [
            [5, 17, 5, 12, 11, 6, 4],
            [10, 9, 6, 10, 12, 16, 4],
            [9, 3, 2, 6, 13, 14, 8],
            [13, 1, 7, 11, 7, 18, 19],
            [1, 7, 12, 8, 3, 1, 5],
            [3, 11, 13, 9, 14, 20, 21],
            [10, 2, 6, 6, 15, 15, 22]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]

        ]
        expected_function_value = 25

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_4(self):
        spending_matrix = [
            [21, 7, 2, 12, 15, 2, 17],
            [23, 15, 24, 20, 12, 5, 11],
            [17, 24, 4, 17, 2, 22, 15],
            [19, 7, 8, 1, 13, 14, 4],
            [15, 6, 6, 14, 19, 3, 16],
            [23, 6, 5, 19, 15, 11, 19],
            [16, 18, 22, 22, 1, 1, 7]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1]
        ]
        expected_function_value = 38

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_5(self):
        spending_matrix = [
            [2, 4, 5, 10, 4, 6, 8],
            [3, 6, 4, 13, 6, 7, 9],
            [4, 7, 10, 5, 10, 4, 5],
            [6, 5, 12, 4, 7, 5, 4],
            [7, 4, 13, 6, 6, 7, 5],
            [10, 8, 5, 2, 8, 9, 10],
            [11, 9, 4, 8, 4, 5, 4]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        expected_function_value = 24

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_6(self):
        spending_matrix = [
            [7, 9, 4, 6, 4, 12, 3],
            [2, 4, 4, 7, 8, 8, 5],
            [4, 5, 6, 5, 12, 7, 3],
            [3, 6, 8, 4, 6, 6, 7],
            [5, 10, 9, 3, 8, 5, 4],
            [6, 9, 5, 10, 9, 6, 7],
            [7, 4, 3, 6, 2, 3, 4]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        expected_function_value = 25

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_7(self):
        spending_matrix = [
            [6, 7, 8, 9, 10, 12, 5],
            [2, 3, 4, 8, 9, 16, 8],
            [9, 6, 3, 6, 8, 9, 3],
            [5, 7, 6, 7, 10, 7, 8],
            [4, 8, 18, 8, 6, 2, 3],
            [12, 9, 2, 10, 8, 4, 5],
            [3, 10, 3, 5, 4, 3, 8]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0]
        ]
        expected_function_value = 27

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_8(self):
        spending_matrix = [
            [12, 4, 8, 9, 12, 4, 5],
            [6, 5, 10, 7, 3, 6, 8],
            [3, 10, 4, 12, 5, 6, 10],
            [11, 12, 16, 5, 7, 8, 12],
            [6, 7, 4, 6, 7, 2, 1],
            [12, 5, 7, 12, 9, 4, 5],
            [4, 6, 8, 4, 3, 6, 7]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0]
        ]
        expected_function_value = 25

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_9(self):
        spending_matrix = [
            [6, 3, 5, 4, 6, 7, 8],
            [5, 2, 4, 3, 8, 9, 10],
            [4, 3, 3, 5, 4, 6, 7],
            [7, 5, 3, 2, 1, 4, 5],
            [8, 6, 6, 10, 12, 5, 4],
            [12, 7, 8, 7, 4, 8, 9],
            [4, 8, 9, 6, 7, 4, 3]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1]

        ]
        expected_function_value = 25

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_10(self):
        spending_matrix = [
            [4, 3, 5, 4, 8, 9, 10],
            [7, 6, 2, 5, 12, 13, 4],
            [6, 5, 1, 6, 7, 8, 9],
            [7, 4, 6, 10, 4, 7, 3],
            [4, 3, 10, 8, 5, 3, 2],
            [3, 8, 12, 6, 3, 6, 12],
            [5, 9, 4, 7, 8, 9, 1]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1]
        ]
        expected_function_value = 20

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_vadim(self):
        spending_matrix = [
            [8, 3, 8, 12, 8],
            [9, 8, 7, 8, 4],
            [5, 2, 2, 4, 2],
            [8, 10, 9, 14, 3],
            [9, 3, 7, 10, 5]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
        ]
        expected_function_value = 24

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)

    def test_solve_theory_example(self):
        spending_matrix = [
            [3, 10, 5, 9, 16],
            [6, 8, 11, 8, 18],
            [7, 13, 10, 3, 4],
            [5, 9, 6, 21, 12],
            [5, 4, 11, 6, 13]
        ]
        table = HMTable(spending_matrix)
        expected_result_matrix = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0]
        ]
        expected_function_value = 25

        result, function_value = solve_hm_table(table)

        self.assertTrue(np.array_equal(expected_result_matrix, result))
        self.assertEqual(expected_function_value, function_value)


if __name__ == "__main__":
    unittest.main()
