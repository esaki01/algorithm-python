import unittest
from algorithm.searching.binary_search import BinarySearch


class TestLinearSearch(unittest.TestCase):

    data = [11, 13, 17, 19, 23, 29, 31]

    def test_search_target_found(self):
        target = 17
        expected = 2

        actual = BinarySearch.search(self.data, target)

        self.assertEqual(expected, actual)

    def test_search_target_not_found(self):
        target = 18
        expected = -1

        actual = BinarySearch.search(self.data, target)

        self.assertEqual(expected, actual)
