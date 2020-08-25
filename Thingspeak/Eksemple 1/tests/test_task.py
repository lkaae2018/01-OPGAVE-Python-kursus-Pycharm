import unittest

from ..Temp_fugt import sum


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(1, 2), 3, msg="adds 1 + 2 to equal 3")
