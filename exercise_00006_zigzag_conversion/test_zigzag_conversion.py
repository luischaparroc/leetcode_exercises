import unittest

from exercise_00006_zigzag_conversion.zigzag_conversion import convert


class ZigzagConversionTestCase(unittest.TestCase):

    def test_example_1(self):
        result = convert(s='PAYPALISHIRING', numRows=3)
        self.assertEqual(result, 'PAHNAPLSIIGYIR')

    def test_example_2(self):
        result = convert(s='PAYPALISHIRING', numRows=4)
        self.assertEqual(result, 'PINALSIGYAHRPI')
