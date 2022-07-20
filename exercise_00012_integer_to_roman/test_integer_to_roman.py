import unittest

from exercise_00012_integer_to_roman.integer_to_roman import int_to_roman


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        result = int_to_roman(3)
        self.assertEqual(result, 'III')

    def test_example_2(self):
        result = int_to_roman(58)
        self.assertEqual(result, 'LVIII')

    def test_example_3(self):
        result = int_to_roman(1994)
        self.assertEqual(result, 'MCMXCIV')
