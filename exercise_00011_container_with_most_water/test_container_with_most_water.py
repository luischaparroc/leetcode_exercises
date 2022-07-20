import unittest

from exercise_00011_container_with_most_water.container_with_most_water import maxArea


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        result = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(result, 49)

    def test_example_2(self):
        result = maxArea([3, 9, 3, 4, 7, 2, 12, 6])
        self.assertEqual(result, 45)
