import unittest

from src.algorithms.searching.hashing import Hashing


class TestLinearSearch(unittest.TestCase):

    data = [12, 25, 36, 20, 30, 8, 42]

    def test_search_target_found(self):
        target = 36
        expected = 4

        hash_data = Hashing.store(self.data)
        actual = Hashing.search(hash_data, target)

        self.assertEqual(expected, actual)

    def test_search_target_not_found(self):
        target = 37
        expected = -1

        hash_data = Hashing.store(self.data)
        actual = Hashing.search(hash_data, target)

        self.assertEqual(expected, actual)
