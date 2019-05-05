import unittest
from algorithm.sorting.insertion_sort import InsertionSort


class TestLinearSearch(unittest.TestCase):

    def test_sort(self):
        data = [5, 3, 4, 1, 2]
        expected = [1, 2, 3, 4, 5]

        InsertionSort.sort(data)

        self.assertEqual(expected, data)
