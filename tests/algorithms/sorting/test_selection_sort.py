import unittest

from src.algorithms.sorting.selection_sort import SelectionSort


class TestSelectionSort(unittest.TestCase):

    def test_sort(self):
        data = [12, 13, 11, 14, 10]
        expected = [10, 11, 12, 13, 14]

        SelectionSort.sort(data)

        self.assertEqual(expected, data)
