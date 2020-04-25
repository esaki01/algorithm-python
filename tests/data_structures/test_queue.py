import unittest

from src.data_structures.queue import Queue


class TestQueue(unittest.TestCase):

    def test_queue(self):
        alist = Queue()
        alist.enqueue(1)
        alist.enqueue(2)
        alist.enqueue(3)

        self.assertEqual(1, alist.dequeue())
        self.assertEqual([2, 3], alist.queue)
