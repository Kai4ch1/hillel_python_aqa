import unittest
from xmlrpc.client import Boolean

from hillel_python_aqa.lesson_12.homeworks.homeworks import *


class TestPreviousHomeWork(unittest.TestCase):
    def test_for_homework_number_1(self):
        test_data = "hhhhHHHH"

        actual_result = task_1(test_data)
        expected_result = 8

        self.assertEqual(expected_result, actual_result)

    def test_for_empty_str(self):
        test_data = ""
        actual_result = task_1(test_data)
        expected_result = 0

        self.assertEqual(expected_result, actual_result)

    def test_string_without_seeking_char(self):
        test_data = "qweqweqweASDASDEi4"

        actual_result = task_1(test_data)
        expected_result = 0

        self.assertEqual(actual_result, expected_result)

    def test_smoke_for_homework_task_2(self):
        test_data = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        actual_result = task_2(test_data)
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']

        self.assertEqual(expected_result, actual_result)

    def test_type_for_homework_task_2(self):
        test_data = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        actual_result = task_2(test_data)
        self.assertIsInstance(actual_result, list)

    def test_task_2_without_str(self):
        test_data = [1, (1,3,5), None, True, Boolean]
        actual_result = task_2(test_data)

        self.assertEqual(actual_result, [])

    def test_negative_with_empty_list(self):
        test_data = []
        actual_result = task_2(test_data)
        expected_result = []

        self.assertEqual(expected_result, actual_result)


    def test_zero_division_for_task_3(self):

        with self.assertRaises(ZeroDivisionError):
            task_3(3, 0)

    def test_function_remains_after_division(self):

        actual_result = task_3(7, 3)
        self.assertIsInstance(actual_result, float)

    def test_function_with_negative_numbers(self):

        actual_result = task_3(9, -2)
        expected_result = -4.5

        self.assertEqual(expected_result, actual_result)




if __name__ == "__main__":
    unittest.main()


