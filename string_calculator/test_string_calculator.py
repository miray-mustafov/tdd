import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def test_should_return_zero_on_empty_string(self):
        actual = StringCalculator().add('')
        self.assertEqual(actual, 0)

    def test_should_return_the_value_on_single_num(self):
        actual = StringCalculator().add('1')
        actual2 = StringCalculator().add('2')

        self.assertEqual(actual, 1)
        self.assertEqual(actual2, 2)

    def test_should_return_correct_sum_when_2_numbers_passed(self):
        actual = StringCalculator().add('1,2')
        self.assertEqual(actual, 3)

    def test_should_return_correct_sum_when_more_numbers_passed(self):
        actual = StringCalculator().add('1,1,1,1')
        self.assertEqual(actual, 4)


    def test_should_return_correct_sum_when_mixed_separators_passed(self):
        actual = StringCalculator().add('1\n2,3')
        self.assertEqual(actual, 6)

