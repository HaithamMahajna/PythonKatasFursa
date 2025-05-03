import unittest
from katas.do_n_times import do_n_times


class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        arr = []
        def append_():
            arr.append(0)
        do_n_times(append_,5)
        self.assertEqual(arr, [0,0,0,0,0])