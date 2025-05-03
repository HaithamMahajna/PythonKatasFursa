import unittest
from katas.true_counter import count_true_values


class TestTrueCounter(unittest.TestCase):
    def test_true_counter(self):
        sample_array = [True, False, True, True, False]
        self.assertEqual(count_true_values(sample_array),3)
