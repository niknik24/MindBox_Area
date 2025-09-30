import unittest
from areaFinder import areaFinder


class TestAreaFinder(unittest.TestCase):

    def setUp(self):
        self.finder = areaFinder()

    def test_circle(self):
        self.assertAlmostEqual(self.finder.circle_area(1.0), 3.1415926, places=3)
        self.assertAlmostEqual(self.finder.circle_area(5.0), 78.53981, places=3)
        self.assertAlmostEqual(self.finder.circle_area(10.0), 314.1592, places=3)
        self.assertEqual(self.finder.circle_area(-1.0), -1.0)  # Non valid
        self.assertEqual(self.finder.find_area([-3.0]), -1.0)  # Not knowing if circle, non valid
        self.assertAlmostEqual(self.finder.find_area([2.0]), 12.56637, places=3)  # Not knowing if circle

    def test_triangle(self):
        self.assertAlmostEqual(self.finder.triangle_area([2.0, 4.0, 5.0]), 3.799671, places=3)
        self.assertAlmostEqual(self.finder.triangle_area([7.0, 4.0, 5.0]), 9.797958, places=3)
        self.assertAlmostEqual(self.finder.triangle_area([10.0, 11.0, 12.0]), 51.521233, places=3)
        self.assertAlmostEqual(self.finder.triangle_area([3.0, 4.0, 5.0]), 6.0, places=3)  # Right-angled
        self.assertAlmostEqual(self.finder.triangle_area([4.0, 1.0, 2.0]), -1.0, places=3)  # Non valid
        self.assertAlmostEqual(self.finder.triangle_area([-4.0, 1.0, 2.0]), -1.0, places=3)  # Non valid side
        self.assertAlmostEqual(self.finder.find_area([1.0, 4.0, 7.0]), -1.0, places=3)  # Not knowing if triangle,
        # non valid
        self.assertAlmostEqual(self.finder.find_area([2.0, 4.0, 5.0]), 3.799671, places=3)  # Not knowing if triangle


    def test_rectangle(self):
        self.assertAlmostEqual(self.finder.rectangle_area([3.0, 3.0, 4.0, 4.0]), 12.0, places=3)
        self.assertAlmostEqual(self.finder.rectangle_area([2.0, 2.0, 7.0, 7.0]), 14.0, places=3)
        self.assertAlmostEqual(self.finder.rectangle_area([6.3, 6.3, 5.9, 5.9]), 37.17, places=3)
        self.assertAlmostEqual(self.finder.rectangle_area([5.0, 5.0, 5.0, 5.0]), 25.0, places=3)
        self.assertAlmostEqual(self.finder.rectangle_area([5.0, 4.0, 3.0, 2.0]), -1.0, places=3)  # Non valid
        self.assertAlmostEqual(self.finder.find_area([3.0, 3.0, 6.0, 6.0]), 18.0, places=3)  # Not knowing if rectangle
        self.assertAlmostEqual(self.finder.find_area([3.0, 1.0, 6.0, 3.0]), -1.0, places=3)  # Not knowing if rectangle,
        # non valid
