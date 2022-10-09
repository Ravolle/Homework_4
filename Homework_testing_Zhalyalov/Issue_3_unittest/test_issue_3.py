import Issue_3_unittest
from Issue_3_unittest import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_fit_transform_equal(self):
        actual1 = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected1 = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual1, expected1)

        actual2 = fit_transform(['123', '321', '123', '546', '555', '123'])
        expected2 = [
            ('123', [0, 0, 0, 1]),
            ('321', [0, 0, 1, 0]),
            ('123', [0, 0, 0, 1]),
            ('546', [0, 1, 0, 0]),
            ('555', [1, 0, 0, 0]),
            ('123', [0, 0, 0, 1])
        ]
        self.assertEqual(actual2, expected2)

    def test_fit_transform_notin(self):
        actual = fit_transform('London')
        place = [
            [('London', [7])],
            [('New York', [4])],
            [('London', [3])],
            [('Moscow', [0])],
            [('London', [2])]
        ]
        self.assertNotIn(actual, place)

    def test_fit_transform_exception(self):
        self.assertRaises(TypeError, Issue_3_unittest.fit_transform, )
