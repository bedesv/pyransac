"""Test case for the ransac module.

This module contains tests for the ransac module.
"""

# Standard library imports
import unittest

# Local application imports
from pyransac import ransac
from pyransac import line2d


class TestRansac(unittest.TestCase):
    """Test the ransac module.

    """
    def test_ransac_params(self) -> None:
        """Test RansacParams initialization.

        :return: None
        """
        params = ransac.RansacParams(samples=1,
                                     iterations=2,
                                     confidence=3,
                                     threshold=4)

        self.assertEqual(params.samples, 1)
        self.assertEqual(params.iterations, 2)
        self.assertEqual(params.confidence, 3)
        self.assertEqual(params.threshold, 4)

    def test_find_inliers(self) -> None:
        """Test the ransac find_inliers function.

        :return: None
        """
        test_inliers = [line2d.Point2D(x, x) for x in range(0, 10)]
        test_outliers = [line2d.Point2D(5, 1),
                         line2d.Point2D(5, 2),
                         line2d.Point2D(6, 1),
                         line2d.Point2D(5, 2)]
        test_data = test_inliers + test_outliers
        ransac_params = ransac.RansacParams(samples=2,
                                            iterations=10,
                                            confidence=0.999,
                                            threshold=1)

        test_model = line2d.Line2D()

        inliers = ransac.find_inliers(points=test_data,
                                      model=test_model,
                                      params=ransac_params)

        self.assertEqual(sorted(test_inliers), sorted(inliers))

    def test_no_outliers(self) -> None:
        """Test that RANSAC functions given all inliers.

        :return: None
        """
        test_data = [line2d.Point2D(x, x) for x in range(0, 10)]
        ransac_params = ransac.RansacParams(samples=2,
                                            iterations=10,
                                            confidence=0.999,
                                            threshold=1)

        test_model = line2d.Line2D()

        inliers = ransac.find_inliers(points=test_data,
                                      model=test_model,
                                      params=ransac_params)

        self.assertEqual(sorted(test_data), sorted(inliers))

    def test_empty_point_list(self):
        """Test case where the point list is empty.

        The function should return an empty list when no points are given.
        """
        model = line2d.Line2D()
        params = ransac.RansacParams(samples=2, iterations=10, confidence=0.95, threshold=0.5, expected_angle=45)
        self.assertEqual(ransac.find_inliers_custom([], model, params), [])

    def test_single_point(self):
        """Test case with a single point in the list.

        The function should return an empty list since a line cannot be formed with a single point.
        """
        model = line2d.Line2D()
        point = line2d.Point2D(1, 1)
        params = ransac.RansacParams(samples=2, iterations=10, confidence=0.95, threshold=0.5, expected_angle=45)
        self.assertEqual(ransac.find_inliers_custom([point], model, params), [])

    def test_multiple_points(self):
        """Test case with multiple points in the list.

        This test verifies if the returned result meets the conditions of having a performance score and being within the top 10 models.
        """
        model = line2d.Line2D()
        points = [line2d.Point2D(i, i) for i in range(1, 11)]
        params = ransac.RansacParams(samples=2, iterations=1000, confidence=0.95, threshold=0.5, expected_angle=45)
        results = ransac.find_inliers_custom(points, model, params)
        self.assertTrue(all(r[0] >= 0 for r in results))
        self.assertTrue(len(results) <= 10)

    def test_tolerance(self):
        """Test case for the model angle tolerance.

        This test checks if the returned models fall within the model angle tolerance specified in the `RansacParams`.
        """
        model = line2d.Line2D()
        points = [line2d.Point2D(i, 2 * i) for i in range(1, 11)]
        params = ransac.RansacParams(samples=2, iterations=1000, confidence=0.95, threshold=0.5, expected_angle=63.43)
        self.assertIsNone(model.angle)
        ransac.find_inliers_custom(points, model, params)
        self.assertTrue(abs(model.angle - params.expected_angle) < 10)


if __name__ == '__main__':
    unittest.main()
