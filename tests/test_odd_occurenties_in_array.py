import unittest
from lessons.odd_occurencies_in_array import *


class MyTestCases(unittest.TestCase):
    def test(self):
        self.assertEqual(find_odd_number([9, 3, 9, 3, 9, 7, 9]), 7)
