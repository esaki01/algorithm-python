import unittest

from src.data_structure.stack import Stack


class TestStack(unittest.TestCase):

    def test_stack(self):
        alist = Stack()
        alist.push(1)
        alist.push(2)
        alist.push(3)

        self.assertEqual(3, alist.pop())
        self.assertEqual([1, 2], alist.stack)
