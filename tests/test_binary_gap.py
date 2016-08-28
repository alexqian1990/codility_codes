import unittest
from lessons.binary_gap import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(compute(9), 2)
        self.assertEqual(compute(529),4)
        self.assertEqual(compute(20),1)
        self.assertEqual(compute(15),0)


if __name__ == '__main__':
    unittest.main()
