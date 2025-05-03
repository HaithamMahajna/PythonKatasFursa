import unittest
from katas.reduce_list import reduce_array


class TestReduceList(unittest.TestCase):
    def test_reduce_list(self):
        sample_list = [10,15,7,20,25]
        reduce_array(sample_list)
        self.assertEqual(sample_list,[10, 5, -8, 13, 5])
