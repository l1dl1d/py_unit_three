import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.add_two(7, 8))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        # Add two more tests of your own below here
        self.assertEqual(20, return_addtion.add_two(10, 10))
        self.assertEqual(5, return_addtion.add_two(6,-1))
    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.area(3, 4, 5))
        self.assertEqual(30, triangle_area.area(5, 13, 12))
        self.assertEqual(24, triangle_area.area(8, 10, 6))
if __name__ == '__main__':
    unittest.main()
