import unittest

from exercise_00008_string_to_integer.string_to_integer import myAtoi


class StringToIntegerTestCase(unittest.TestCase):

    def test_example_1(self):
        result = myAtoi('42')
        self.assertEqual(result, 42)

    def test_example_2(self):
        result = myAtoi('     -42')
        self.assertEqual(result, -42)

    def test_example_3(self):
        result = myAtoi('4193 with words')
        self.assertEqual(result, 4193)
