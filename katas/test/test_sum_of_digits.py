import unittest
from katas.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("45"), 9)
