import unittest
from katas.list_diff import find_difference


class TestIsUniqueStr(unittest.TestCase):
    def test_list_diff(self):
        l1 = [10,3,-49,0,1]
        self.assertEqual(find_difference(l1), max(l1)-min(l1))
