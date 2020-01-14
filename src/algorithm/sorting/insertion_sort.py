class InsertionSort:

    @staticmethod
    def sort(data: list):
        for i in range(1, len(data)):
            tmp = data[i]
            k = i
            while k > 0 and data[k - 1] > tmp:
                data[k] = data[k - 1]
                k -= 1
            data[k] = tmp
