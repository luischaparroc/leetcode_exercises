import unittest

from exercise_00005_longest_palindromic_substring.longest_palindromic_substring import (
    longestPalindrome
)


class LongestPalindromeTestCase(unittest.TestCase):

    def test_example_1(self):
        result = longestPalindrome('babad')
        self.assertEqual(result, 'bab')

    def test_example_2(self):
        result = longestPalindrome('cbbd')
        self.assertEqual(result, 'bb')
