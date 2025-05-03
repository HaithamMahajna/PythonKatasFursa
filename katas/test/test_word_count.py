import unittest
from katas.word_count import count_words



class TestWordCount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(count_words("Hello world"), 2)

