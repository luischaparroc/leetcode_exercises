import unittest

from exercise_00003_length_of_longest_substring.length_of_longest_substring import (
    lengthOfLongestSubstring
)


class LengthOfLongestSubstringTestCase(unittest.TestCase):

    def test_example_1(self):
        result = lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(result, 3)

    def test_example_2(self):
        result = lengthOfLongestSubstring('bbbbb')
        self.assertEqual(result, 1)

    def test_example_3(self):
        result = lengthOfLongestSubstring('pwwkew')
        self.assertEqual(result, 3)
