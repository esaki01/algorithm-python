class BubbleSort:

    @staticmethod
    def sort(data: list):
        for k in range(len(data) - 1):
            for i in range(len(data) - 1, k, -1):
                if data[i - 1] > data[i]:
                    tmp = data[i - 1]
                    data[i - 1] = data[i]
                    data[i] = tmp
