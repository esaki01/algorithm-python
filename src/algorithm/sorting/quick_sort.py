class QuickSort:

    @staticmethod
    def sort(data: list):
        QuickSort._sort(data, 0, len(data) - 1)

    @staticmethod
    def _sort(data: list, left: int, right: int):
        pl = left
        pr = right
        pivot = data[(pl + pr) // 2]

        while pl <= pr:
            while data[pl] < pivot and pl < right:
                pl += 1

            while data[pr] > pivot and pr > left:
                pr -= 1

            if pl <= pr:
                tmp = data[pl]
                data[pl] = data[pr]
                data[pr] = tmp

                pl += 1
                pr -= 1

        if left < pr:
            QuickSort._sort(data, left, pr)

        if pl < right:
            QuickSort._sort(data, pl, right)
