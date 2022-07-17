import unittest

from exercise_00007_reverse_integer.reverse_integer import reverse


class ReverseIntegerTestCase(unittest.TestCase):

    def test_example_1(self):
        result = reverse(123)
        self.assertEqual(result, 321)

    def test_example_2(self):
        result = reverse(-123)
        self.assertEqual(result, -321)

    def test_example_3(self):
        result = reverse(120)
        self.assertEqual(result, 21)
