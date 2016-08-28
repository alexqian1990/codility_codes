import unittest
from lessons.binary_gap import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(compute(9), compute_simpler(9))
        self.assertEqual(compute(529), compute_simpler(529))
        self.assertEqual(compute(20), compute_simpler(20))
        self.assertEqual(compute(15), compute_simpler(15))


if __name__ == '__main__':
    unittest.main()
