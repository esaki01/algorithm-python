class BinarySearch:

    @staticmethod
    def search(data: list, target: int) -> int:
        head = 0
        tail = len(data) - 1
        while head <= tail:
            center = (head + tail) // 2
            if data[center] == target:
                return center
            elif data[center] < target:
                head = center + 1
            else:
                tail = center - 1
        return -1
