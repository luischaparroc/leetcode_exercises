import unittest

from exercise_00329_is_subsequence.is_subsequence import is_subsequence


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        result = is_subsequence("abc", "ahbgdc")
        self.assertTrue(result)

    def test_example_2(self):
        result = is_subsequence("axc", "ahbgdc")
        self.assertFalse(result)

    def test_example_3(self):
        result = is_subsequence("", "ahbgdc")
        self.assertTrue(result)
