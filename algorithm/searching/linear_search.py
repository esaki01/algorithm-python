class LinearSearch:

    @staticmethod
    def search(data: list, target: int) -> int:
        for i, d in enumerate(data):
            if d == target:
                return i
        return -1

        # for i, d1 in enumerate(data):
        #     min = d1
        #     for j, d2 in enumerate(data):
        #         if d2 < d1:
        #             min = d2
