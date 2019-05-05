class SelectionSort:

    @staticmethod
    def sort(data: list):
        for i in range(len(data) - 1):
            index_min = i
            for k in range(i + 1, len(data)):
                if data[k] < data[index_min]:
                    index_min = k

            tmp = data[i]
            data[i] = data[index_min]
            data[index_min] = tmp
