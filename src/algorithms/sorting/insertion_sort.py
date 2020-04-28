class InsertionSort:

    @staticmethod
    def sort(data: list):
        for i in range(1, len(data)):
            tmp = data[i]
            k = i - 1
            while k >= 0 and data[k] > tmp:
                data[k + 1] = data[k]
                k -= 1
            data[k + 1] = tmp
