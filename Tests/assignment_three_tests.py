import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(6, assignment_three.area(2,3))
        self.assertEqual(8, assignment_three.area(2,4))
        self.assertEqual(150, assignment_three.surface_area(4,3,9))
if __name__ == '__main__':
    unittest.main()
