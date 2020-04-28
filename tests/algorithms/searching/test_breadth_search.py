import unittest

from src.algorithms.searching.breadth_search import BreadthSearch


class TestBreadthSearch(unittest.TestCase):

    tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

    def test_search(self):
        BreadthSearch.search(self.tree)
