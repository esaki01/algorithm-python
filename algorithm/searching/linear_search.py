class LinearSearch:

    @staticmethod
    def search(data: list, target: int) -> int:
        for i, d in enumerate(data):
            if d == target:
                return i
        return -1
