import unittest
from seminar13.taskDZ_01 import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)
        self.r3 = Rectangle(8, 9.0)

    def test_width(self):
        self.assertEqual(self.r1.width, 5, msg='FAILED (failures=1)')

    def test_height(self):
        self.assertEqual(self.r2.height, 4, msg='FAILED (failures=1)')

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 20, msg='FAILED (failures=1)')

    def test_area(self):
        self.assertEqual(self.r2.area(), 12, msg='FAILED (failures=1)')

    def test_addition(self):
        r3 = self.r1 + self.r2
        self.assertEqual(self.r3.__eq__(r3), True, msg='FAILED (failures=1)')


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main()