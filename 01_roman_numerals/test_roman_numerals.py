import unittest
from roman_numerals import convert_to_roman


class TestRomanNumeralsConvert(unittest.TestCase):
    def test_convert_returns_I_when_1_passed(self):
        actual = convert_to_roman(1)
        self.assertEqual(actual, 'I')

    def test_convert_returns_IV_when_4_passed(self):
        actual = convert_to_roman(4)
        self.assertEqual(actual, 'IV')

    def test_convert_returns_VIII_when_8_passed(self):
        actual = convert_to_roman(8)
        self.assertEqual(actual, 'VIII')

    def test_convert_returns_IX_when_9_passed(self):
        actual = convert_to_roman(9)
        self.assertEqual(actual, 'IX')

    def test_convert_returns_XLIV_when_44_passed(self):
        actual = convert_to_roman(44)
        self.assertEqual(actual, 'XLIV')

    def test_convert_returns_CXCIX_when_199_passed(self):
        actual = convert_to_roman(199)
        self.assertEqual(actual, 'CXCIX')

    def test_convert_returns_CC_when_200_passed(self):
        actual = convert_to_roman(200)
        self.assertEqual(actual, 'CC')

    def test_convert_returns_CDLXVIII_when_468_passed(self):
        actual = convert_to_roman(468)
        self.assertEqual(actual, 'CDLXVIII')

    def test_convert_returns_MCMXCVIII_when_1998_passed(self):
        actual = convert_to_roman(1998)
        self.assertEqual(actual, 'MCMXCVIII')

    def test_convert_returns_MMMCMXCIX_when_3999_passed(self):
        """3999 is the largest number convertable to traditional Roman"""
        actual = convert_to_roman(3999)
        self.assertEqual(actual, 'MMMCMXCIX')


    def test_convert_returns_error_when_4000_passed(self):
        self.assertRaises(Exception, convert_to_roman, 4000)


