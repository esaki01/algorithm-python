from typing import List


class BreadthSearch:

    @staticmethod
    def search(tree: List[List]):
        data = [0]
        while len(data) > 0:
            pos = data.pop(0)
            print(pos, end=" ")
            for i in tree[pos]:
                data.append(i)
