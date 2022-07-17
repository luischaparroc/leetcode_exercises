import unittest

from exercise_00009_palindrome_number.palindrome_number import isPalindrome


class ReverseIntegerTestCase(unittest.TestCase):

    def test_example_1(self):
        result = isPalindrome(121)
        self.assertTrue(result)

    def test_example_2(self):
        result = isPalindrome(-121)
        self.assertFalse(result)

    def test_example_3(self):
        result = isPalindrome(10)
        self.assertFalse(result)
