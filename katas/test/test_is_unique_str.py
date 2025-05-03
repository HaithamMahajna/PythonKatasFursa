import unittest
from katas.is_unique_str import is_unique


class TestIsUniqueStr(unittest.TestCase):

    def test_all_unique(self):
        self.assertTrue(is_unique("abc"))

    def test_with_duplicates(self):
        self.assertFalse(is_unique("hello"))

    def test_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_single_char(self):
        self.assertTrue(is_unique("x"))

    def test_numbers(self):
        self.assertTrue(is_unique("1234"))
        self.assertFalse(is_unique("1123"))
