import unittest

from exercise_01480_running_sum_of_1d_array.running_sum_of_1d_array import running_sum


class RunningSumOf1dArrayTestCase(unittest.TestCase):

    def test_example_1(self):
        result = running_sum([1, 2, 3, 4])
        self.assertEqual(result, [1, 3, 6, 10])

    def test_example_2(self):
        result = running_sum([1,1,1,1,1])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_example_3(self):
        result = running_sum([3, 1, 2, 10, 1])
        self.assertEqual(result, [3, 4, 6, 16, 17])
