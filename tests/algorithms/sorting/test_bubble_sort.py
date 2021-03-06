import unittest

from src.algorithms.sorting.bubble_sort import BubbleSort


class TestBubbleSort(unittest.TestCase):

    def test_sort(self):
        data = [5, 3, 4, 1, 2]
        expected = [1, 2, 3, 4, 5]

        BubbleSort.sort(data)

        self.assertEqual(expected, data)
