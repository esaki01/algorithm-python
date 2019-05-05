import unittest
from algorithm.sorting.quick_sort import QuickSort


class TestLinearSearch(unittest.TestCase):

    def test_sort(self):
        data = [5, 4, 7, 6, 8, 3, 1, 2, 9]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        QuickSort.sort(data)

        self.assertEqual(expected, data)
