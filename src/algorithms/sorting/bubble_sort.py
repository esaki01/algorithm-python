class BubbleSort:

    @staticmethod
    def sort(data: list):
        for k in range(len(data) - 1):
            for i in range(len(data) - 1 - k):
                if data[i] > data[i + 1]:
                    tmp = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = tmp
