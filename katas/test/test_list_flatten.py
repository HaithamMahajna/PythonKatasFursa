import unittest
from katas.list_flatten import flatten_list


class TestIsUniqueStr(unittest.TestCase):
    def test_list_flatten(self):
        list1 = flatten_list ([[1,2,5],[[7,5]],[[[9,2],2]]])
        self.assertEqual(list1, [1,2,5,7,5,9,2,2])
