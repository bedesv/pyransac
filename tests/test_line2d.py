"""
est cases for the line2d module.

This module contains tests for the 2D line model and error functions.
"""

# Standard library imports
import math
import unittest

from unittest.mock import MagicMock

# Local application imports
import sys
sys.path.insert(0, "/home/bedesv/pyransac")
from pyransac import line2d


class TestLine2D(unittest.TestCase):
    """
		Test the 2D line module.
    """
    def test_point2d(self) -> None:
        """
            Test Point2D class initialization.
        """
        test_point = line2d.Point2D(1, 2)

        self.assertEqual(test_point.x, 1)
        self.assertEqual(test_point.y, 2)




    """
        ************** Point2D Equality **************    
    """

    def test_point2d_eq_true_no_index(self) -> None:
        """
            Test Point2D class equality method without indexes.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 2)

        self.assertEqual(test_point_1, test_point_2)

    def test_point2d_eq_true_with_index(self) -> None:
        """
			Test Point2D class equality method with indexes.
        """
        test_point_1 = line2d.Point2D(1, 2, 5)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertEqual(test_point_1, test_point_2)

    def test_point2d_eq_different_x_no_index(self) -> None:
        """
            Test Point2D class equality method without indexes
            when they have different x values.
        """
        test_point_1 = line2d.Point2D(2, 2)
        test_point_2 = line2d.Point2D(1, 2)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_different_y_no_index(self) -> None:
        """
            Test Point2D class equality method without indexes
            when they have different y values.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 1)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_different_x_with_index(self) -> None:
        """
            Test Point2D class equality method with indexes
            when they have different x values.
        """
        test_point_1 = line2d.Point2D(2, 2, 5)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_different_y_with_index(self) -> None:
        """
            Test Point2D class equality method with indexes
            when they have different y values.
        """
        test_point_1 = line2d.Point2D(1, 2, 5)
        test_point_2 = line2d.Point2D(1, 1, 5)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_different_index(self) -> None:
        """
			Test Point2D class equality method when indexes
            are different.
        """
        test_point_1 = line2d.Point2D(1, 2, 4)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_one_with_index(self) -> None:
        """
			Test Point2D class equality method when only
            one point has an index.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(test_point_1, test_point_2)

    def test_point2d_eq_with_different_type(self) -> None:
        """
			Test Point2D class equality method when testing
            against an integer.
        """
        test_point = line2d.Point2D(1, 2)

        self.assertNotEqual(test_point, 5)



    """
        ************** Point2D Hash **************    
    """

    def test_point2d_hash_true_no_index(self) -> None:
        """
            Test Point2D class hash method without indexes.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 2)

        self.assertEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_true_with_index(self) -> None:
        """
			Test Point2D class hash method with indexes.
        """
        test_point_1 = line2d.Point2D(1, 2, 5)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_different_x_no_index(self) -> None:
        """
            Test Point2D class hash method without indexes
            when they have different x values.
        """
        test_point_1 = line2d.Point2D(2, 2)
        test_point_2 = line2d.Point2D(1, 2)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_different_y_no_index(self) -> None:
        """
            Test Point2D class hash method without indexes
            when they have different y values.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 1)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_different_x_with_index(self) -> None:
        """
            Test Point2D class hash method with indexes
            when they have different x values.
        """
        test_point_1 = line2d.Point2D(2, 2, 5)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_different_y_with_index(self) -> None:
        """
            Test Point2D class hash method with indexes
            when they have different y values.
        """
        test_point_1 = line2d.Point2D(1, 2, 5)
        test_point_2 = line2d.Point2D(1, 1, 5)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_different_index(self) -> None:
        """
			Test Point2D class hash method when indexes
            are different.
        """
        test_point_1 = line2d.Point2D(1, 2, 4)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))

    def test_point2d_hash_one_with_index(self) -> None:
        """
			Test Point2D class hash method when only
            one point has an index.
        """
        test_point_1 = line2d.Point2D(1, 2)
        test_point_2 = line2d.Point2D(1, 2, 5)

        self.assertNotEqual(hash(test_point_1), hash(test_point_2))




    """
        ************** Line2D Initialisation **************    
    """

    def test_line2d_init_none(self) -> None:
        """
			Test 2D line model initialization without parameters.
        """
        test_model = line2d.Line2D()

        self.assertIs(test_model.slope, None)
        self.assertIs(test_model.y_int, None)
        self.assertIs(test_model.x_int, None)

    def test_line2d_init_args(self) -> None:
        """
			Test 2D line model initialization with parameters.
        """
        test_model = line2d.Line2D(slope=1, y_int=2, x_int=3)

        self.assertEqual(test_model.slope, 1)
        self.assertEqual(test_model.y_int, 2)
        self.assertEqual(test_model.x_int, 3)




    """
        ************** Line2D Make Model **************    
    """

    def test_make_model_args(self) -> None:
        """
			Test 2D line model make_model with args != 2.
        """
        test_model = line2d.Line2D()

        self.assertRaises(ValueError, test_model.make_model, [])
        self.assertRaises(ValueError, test_model.make_model, [(1, 1)])
        self.assertRaises(ValueError, test_model.make_model, [(1, 1) * 3])

    def test_make_model_vertical(self) -> None:
        """
			Test 2D line model against vertical line.
        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=1, y=0), line2d.Point2D(x=1, y=10)]

        test_model.make_model(test_data)

        self.assertTrue(math.isnan(test_model.slope))
        self.assertTrue(math.isnan(test_model.y_int))
        self.assertEqual(test_model.x_int, 1)

    def test_make_model_horizontal(self) -> None:
        """
			Test 2D line model against horizontal line.
        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=1, y=10), line2d.Point2D(x=10, y=10)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, 0)
        self.assertEqual(test_model.y_int, 10)
        self.assertIs(test_model.x_int, math.nan)

    def test_make_model_positive(self) -> None:
        """
			Test 2D line model against line with positive slope.
        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=0, y=1), line2d.Point2D(x=1, y=2)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, 1)
        self.assertEqual(test_model.y_int, 1)
        self.assertEqual(test_model.x_int, -1)

    def test_make_model_negative(self) -> None:
        """
			Test 2D line model against line with negative slope.
        """
        test_model = line2d.Line2D()
        test_data = [line2d.Point2D(x=0, y=2), line2d.Point2D(x=1, y=1)]

        test_model.make_model(test_data)

        self.assertEqual(test_model.slope, -1)
        self.assertEqual(test_model.y_int, 2)
        self.assertEqual(test_model.x_int, 2)




    """
        ************** Line2D Get Error **************    
    """

    def test_get_error_vertical(self) -> None:
        """
			Test 2D line point distance with vertical line.
        """
        test_model = line2d.Line2D(slope=math.nan, y_int=math.nan, x_int=3)
        test_point = line2d.Point2D(1, 2)

        error = test_model.calc_error(point=test_point)

        self.assertEqual(error, 2)

    def test_get_error_horizontal(self) -> None:
        """
			Test 2D line point distance with horizontal line.
        """
        test_model = line2d.Line2D(slope=0, y_int=5, x_int=math.nan)
        test_point = line2d.Point2D(2, 1)

        error = test_model.calc_error(point=test_point)

        self.assertEqual(error, 4)

    def test_get_error_positive(self) -> None:
        """
			Test 2D line point distance with line with positive slope.
        """
        test_model = line2d.Line2D(slope=2, y_int=2, x_int=-1)
        test_point = line2d.Point2D(5, 1)

        error = test_model.calc_error(point=test_point)

        self.assertAlmostEqual(error, 11 * math.sqrt(5) / 5)

    def test_get_line_error_neg(self) -> None:
        """
			Test 2D line point distance with line with negative slope.
        """
        test_model = line2d.Line2D(slope=-3, y_int=3, x_int=1)
        test_point = line2d.Point2D(6, 1)

        error = test_model.calc_error(point=test_point)

        self.assertAlmostEqual(error, 8 * math.sqrt(10) / 5)




    """
        ************** Line2D Find Furthest Points **************    
    """

    def test_find_furthest_apart_points_0_points_given(self) -> None:
        """
			Test furthest point calculation when 0 points are given.
        """
        test_model = line2d.Line2D()

        points = []
        self.assertRaises(ValueError, test_model.find_furthest_apart_points, points)

    def test_find_furthest_apart_points_1_point_given(self) -> None:
        """
			Test furthest point calculation when 1 point is given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2)]
        self.assertRaises(ValueError, test_model.find_furthest_apart_points, points)

    def test_find_furthest_apart_points_2_same_points_given(self) -> None:
        """
			Test furthest point calculation when 2 identical points are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(1, 2)]

        self.assertRaises(ValueError, test_model.find_furthest_apart_points, points)

    def test_find_furthest_apart_points_2_different_points_given(self) -> None:
        """
			Test furthest point calculation when 2 different points are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(1, 3)]
        furthest_points = test_model.find_furthest_apart_points(points)

        self.assertEqual(points, furthest_points)

    def test_find_furthest_apart_points_3_points_given(self) -> None:
        """
			Test furthest point calculation when 3 points are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(1, 3), line2d.Point2D(5, 4)]
        furthest_points = test_model.find_furthest_apart_points(points)

        self.assertIn(points[2], furthest_points)
        self.assertIn(points[0], furthest_points)

    def test_find_furthest_apart_points_3_points_on_perfectly_straight_line_given(self) -> None:
        """
			Test furthest point calculation when 3 point on the same line are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(1, 2), line2d.Point2D(5, 4)]
        furthest_points = test_model.find_furthest_apart_points(points)

        self.assertIn(points[2], furthest_points)
        self.assertIn(points[0], furthest_points)

    def test_find_furthest_apart_points_10_points_given(self) -> None:
        """
			Test furthest point calculation when 10 points are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(2, 1.9999), line2d.Point2D(3, 2.0001), 
                  line2d.Point2D(4, 2.005), line2d.Point2D(5, 1.994), line2d.Point2D(6, 2.06),
                  line2d.Point2D(7, 2.003), line2d.Point2D(8, 1.9995), line2d.Point2D(9, 1.9998),
                  line2d.Point2D(10, 2.003)]
        
        furthest_points = test_model.find_furthest_apart_points(points)

        for i in range(0, 10):
            if i in [0, 9]:
                self.assertIn(points[i], furthest_points)
            else:
                self.assertNotIn(points[i], furthest_points)

    def test_find_furthest_apart_points_10_points_on_perfectly_straight_line_given(self) -> None:
        """
			Test furthest point calculation when 10 points on the same line are given.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(2, 2), line2d.Point2D(3, 2.), 
                  line2d.Point2D(4, 2), line2d.Point2D(5, 2), line2d.Point2D(6, 2),
                  line2d.Point2D(7, 2), line2d.Point2D(8, 2), line2d.Point2D(9, 2),
                  line2d.Point2D(10, 2)]
        
        furthest_points = test_model.find_furthest_apart_points(points)

        self.assertIn(points[0], furthest_points)
        self.assertIn(points[1], furthest_points)




    """
        ************** Line2D Calculate Slope **************    
    """

    def test_calculate_slope(self) -> None:
        """
			Test slope calculation.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(2, 3)]

        test_model.find_furthest_apart_points = MagicMock(return_value = points)
        slope = test_model.calculate_slope(None)

        expected_answer = 1
        self.assertEqual(expected_answer, slope)

    def test_calculate_slope_different_order(self) -> None:
        """
			Test slope calculation.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(2, 3), line2d.Point2D(1, 2)]

        test_model.find_furthest_apart_points = MagicMock(return_value = points)
        slope = test_model.calculate_slope(None)

        expected_answer = 1
        self.assertEqual(expected_answer, slope)

    def test_calculate_slope_negative_numbers(self) -> None:
        """
			Test slope calculation with some negative numbers.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(-1, -2), line2d.Point2D(-1000, -4000)]

        test_model.find_furthest_apart_points = MagicMock(return_value = points)
        slope = test_model.calculate_slope(None)

        expected_answer = 4
        self.assertEqual(expected_answer, int(slope)) # Cast to int because of floating point inaccuracy

    def test_calculate_slope_negative_numbers_different_order(self) -> None:
        """
			Test slope calculation with some negative numbers.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(-1000, -4000), line2d.Point2D(-1, -2)]

        test_model.find_furthest_apart_points = MagicMock(return_value = points)
        slope = test_model.calculate_slope(None)

        expected_answer = 4
        self.assertEqual(expected_answer, int(slope)) # Cast to int because of floating point inaccuracy

    def test_calculate_slope_horizontal_line(self) -> None:
        """
			Test slope calculation on a horizontal line.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(4, 2)]
        test_model.find_furthest_apart_points = MagicMock(return_value = points)
        slope = test_model.calculate_slope(None)

        expected_answer = 0
        self.assertEqual(expected_answer, slope)

    def test_calculate_slope_vertical_line(self) -> None:
        """
			Test slope calculation on a vertical line.
        """
        test_model = line2d.Line2D()

        points = [line2d.Point2D(1, 2), line2d.Point2D(1, 4)]
        test_model.find_furthest_apart_points = MagicMock(return_value = points)

        self.assertRaises(ZeroDivisionError, test_model.calculate_slope, None)

    def test_calculate_slope_lines_flipped_in_x_axis(self) -> None:
        """
			Test slope calculation returns inverse values for lines that have
            been flipped in the x axis.
        """
        test_model_1 = line2d.Line2D()
        test_model_2 = line2d.Line2D()

        points_1 = [line2d.Point2D(0, 0), line2d.Point2D(5, 4)]
        points_2 = [line2d.Point2D(0, 0), line2d.Point2D(-5, 4)]
        test_model_1.find_furthest_apart_points = MagicMock(return_value = points_1)
        test_model_2.find_furthest_apart_points = MagicMock(return_value = points_2)

        slope_1 = test_model_1.calculate_slope(None)
        slope_2 = test_model_2.calculate_slope(None)

        self.assertNotEqual(slope_1, slope_2)
        self.assertEqual(-1 * slope_1, slope_2)

    def test_calculate_slope_lines_flipped_in_y_axis(self) -> None:
        """
			Test slope calculation returns inverse values for lines that have
            been flipped in the y axis.
        """
        test_model_1 = line2d.Line2D()
        test_model_2 = line2d.Line2D()

        points_1 = [line2d.Point2D(0, 0), line2d.Point2D(5, 4)]
        points_2 = [line2d.Point2D(0, 0), line2d.Point2D(5, -4)]
        test_model_1.find_furthest_apart_points = MagicMock(return_value = points_1)
        test_model_2.find_furthest_apart_points = MagicMock(return_value = points_2)

        slope_1 = test_model_1.calculate_slope(None)
        slope_2 = test_model_2.calculate_slope(None)

        self.assertNotEqual(slope_1, slope_2)
        self.assertEqual(-1 * slope_1, slope_2)

if __name__ == '__main__':
    unittest.main()
