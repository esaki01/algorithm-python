import unittest

from src.algorithm.searching.linear_search import LinearSearch


class TestLinearSearch(unittest.TestCase):

    data = [4, 2, 3, 5, 1]

    def test_search_target_found(self):
        target = 5
        expected = 3

        actual = LinearSearch.search(self.data, target)

        self.assertEqual(expected, actual)

    def test_search_target_not_found(self):
        target = 6
        expected = -1

        actual = LinearSearch.search(self.data, target)

        self.assertEqual(expected, actual)
