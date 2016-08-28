import unittest
from lessons.cyclic_rotation import *

class MyTestCase(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(rotate([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])


if __name__ == '__main__':
    unittest.main()
