import unittest

from exercise_00205_isomorphic_strings.isomorphic_strings import is_isomorphic


class ContainerWithMostWaterTestCase(unittest.TestCase):

    def test_example_1(self):
        result = is_isomorphic("egg", "add")
        self.assertTrue(result)

    def test_example_2(self):
        result = is_isomorphic("foo", "bar")
        self.assertFalse(result)

    def test_example_3(self):
        result = is_isomorphic("paper", "title")
        self.assertTrue(result)
