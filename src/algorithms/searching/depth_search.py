from typing import List


class DepthSearch:

    @staticmethod
    def search_v1(tree: List[List]):
        """行きがけ順."""
        def _search(pos: int):
            print(pos, end=" ")
            for i in tree[pos]:
                _search(i)

        _search(0)

    @staticmethod
    def search_v2(tree: List[List]):
        """帰りがけ順."""
        def _search(pos: int):
            for i in tree[pos]:
                _search(i)
            print(pos, end=" ")

        _search(0)
