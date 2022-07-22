import unittest

from exercise_00724_find_pivot_index.find_pivot_index import pivot_index


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        result = pivot_index([1, 7, 3, 6, 5, 6])
        self.assertEqual(result, 3)

    def test_example_2(self):
        result = pivot_index([1, 2, 3])
        self.assertEqual(result, -1)

    def test_example_3(self):
        result = pivot_index([2, 1, -1])
        self.assertEqual(result, 0)
