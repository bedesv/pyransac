"""2D line module.

This module contains the model for a 2-dimensional line.
"""

# Standard library imports
from __future__ import annotations
from dataclasses import dataclass
import math
from typing import List, Optional
from scipy import spatial
import itertools

# Local application imports
from pyransac.base import Model

@dataclass(order=True)
class Point2D:
    """
    2-dimensional point class.

    This is a simple class to contain Cartesian coordinates of 2D point.
    """

    """x coordinate of point."""
    x: float  # pylint: disable=invalid-name
    
    """y coordinate of point"""
    y: float  # pylint: disable=invalid-name
    
    """Optional: index used to store a reference to the point's place in it's original list"""
    index: Optional[int] = None

    def __eq__(self, other: Point2D):
        if not isinstance(other, Point2D):
            return False
        
        return self.x == other.x and self.y == other.y and self.index == other.index
    
    def __hash__(self):
        return hash((self.x, self.y, self.index))

class Line2D(Model):
    """
        Model for a 2-dimensional line.
    """
    def __init__(self, slope=None, y_int=None, x_int=None):
        self._slope = slope
        self._y_int = y_int
        self._x_int = x_int

    @property
    def slope(self):
        """
            Gets the slope of the model.

            :return: slope of line (None if model not made).
        """
        return self._slope

    @property
    def y_int(self):
        """
            Gets the y intercept of the model.

            :return: y intercept of line (None if model not made).
        """
        return self._y_int

    @property
    def x_int(self):
        """
            Gets the x intercept of the model.

            :return: x intercept of line (None if model not made).
        """
        return self._x_int
    
    def __eq__(self, other) -> bool:
        """
            Overrides the equality function.

            Calls the existing equals within threshold function with a threshold of 0.

            :return: True if lines are equal, False if not.
        """
        return self.equals_within_threshold(other)

    def equals_within_threshold(self, other, threshold=0, check_slope=True, check_x=True, check_y=True) -> bool:
        """
            Checks if the line is equal to the given line within a given threshold

             :return: True if lines are equal within the threshold, False if not.
        """

        if isinstance(other, Line2D) and \
           (not check_x or abs(self.x_int - other.x_int) <= threshold) and \
           (not check_y or abs(self.y_int - other.y_int) <= threshold) and \
           (not check_slope or abs(self.slope - other.slope) <= threshold):
            return True
        return False
    
    def update_slope(self, points: List[Point2D]) -> None:
        """
            Updates the slope of the model using the given points as a basis

            :param points: list of data points to update the slope with
                           assumed they are inliers to the model
            :return: None
        """
        self._slope = self.calculate_slope(points)

    def find_furthest_apart_points(self, points: List[Point2D]) -> List[Point2D]:
        """
            Calculates which pair of points are the furthest apart in the input set

            Calculates a convex hull first because the furthest apart points must be on the convex
            hull.

            Then iterates through the points on the convex hull to find which pair are the furthest
            apart.

            :param points: list of data points - assumed they are approximately in a line but 
                           will work with any set of points
            :return: list containing two points that are the furthest apart of all the input points
        """
        furthest_points = []
        if len(set(points)) < 2:
            raise ValueError(f"Need at least two distinct points to calculate the furthest apart points")
        
        elif len(points) > 2:
            primitive_points = [[point.x, point.y] for point in points]

            # Find the convex hull of the list of points as the furthest apart points must
            # be in the convex hull
            try:
                convex_hull_indices = spatial.ConvexHull(primitive_points).vertices
            except spatial._qhull.QhullError:

                # This error is thrown if the points are all perfectly on the same line
                # In this case, the furthest points don't matter because the slope will
                # be the same no matter what points are used to calculate it
                # Cast to a set first to avoid returning duplicate points
                # Sorted to ensure the same result if run multiple times
                return sorted(list(set(points)))[:2]

            max_distance = 0

            # Iterate over all combinations of the points on the convex hull
            for i, j in itertools.product(convex_hull_indices, convex_hull_indices): 
                # Find the euclidean distance between the points
                distance = math.dist(primitive_points[i], primitive_points[j]) 

                # Update the furthest apart points
                if distance > max_distance:
                    max_distance = distance
                    furthest_points = [primitive_points[i], primitive_points[j]]

            # Convert points back to a list of Point2D objects
            furthest_points = [Point2D(point[0], point[1]) for point in furthest_points]

        elif len(points) == 2:
            furthest_points = points

        return furthest_points

    def calculate_slope(self, points: List[Point2D]) -> float:
        """
            Assumes the input points are inliers of a line
            Uses find_furthest_apart_points to find which points are furthest apart. 
            Using the furthest apart points should minimise the error as using points closer
            together could introduce error in the slope calculation if they're further away from
            the actual slope.

            Original method of the library just used the two first points in the list, which is 
            susceptible to error.

            :param points: list of data points
            :return: float value of the rise/run slope 
        """ 

        furthest_points = self.find_furthest_apart_points(points)
        slope = ((furthest_points[0].y - furthest_points[1].y) / 
                 (furthest_points[0].x - furthest_points[1].x))
        return slope

    def make_model(self, points: List[Point2D]) -> None:
        """
            Makes equation for 2D line given two data points.

            Model parameters are stored internally.

            :param points: list of data points to make model
                (length must be 2)
            :return: None
        """
        if len(points) != 2:
            raise ValueError(f'Need 2 points to make line, not {len(points)}')

        try:
            
            self._slope = self.calculate_slope(points)
        except ZeroDivisionError:
            self._slope = math.nan
            self._y_int = math.nan
            self._x_int = points[0].x
            return

        self._y_int = points[0].y - self._slope * points[0].x

        try:
            self._x_int = -1 * self._y_int / self._slope
        except ZeroDivisionError:
            self._x_int = math.nan

    def calc_error(self, point: Point2D) -> float:
        """
            Calculate error between data point and 2D model.

            :param point: data point to calculate error with
            :return: calculated error
        """
        if self._slope == 0:
            return abs(point.y - self._y_int)

        if self._slope is math.nan:
            return abs(point.x - self._x_int)

        return abs(point.y - self._y_int - self._slope * point.x) / math.sqrt(
            self._slope ** 2 + 1)
