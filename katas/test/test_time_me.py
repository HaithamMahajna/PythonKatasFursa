import unittest
from katas.time_me import measure_execution_time
import time


class TestTimeMe(unittest.TestCase):
    def test_time_me(self):
        def slow_function():
            time.sleep(2)

        duration = measure_execution_time(slow_function)
        self.assertTrue(2000 <= duration <= 2200, f"Duration was {duration}ms")