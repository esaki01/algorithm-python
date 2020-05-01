import unittest

from src.algorithms.searching.depth_search import DepthSearch


class TestDepthSearch(unittest.TestCase):

    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

    def test_search_v1(self):
        DepthSearch.search_v1(self.tree)

    def test_search_v2(self):
        DepthSearch.search_v2(self.tree)
