class Hashing:

    @staticmethod
    def search(hash_data: list, target: int) -> int:
        k = Hashing._hash(target)
        while hash_data[k] != 0:
            if hash_data[k] == target:
                return k
            k = (k + 1) % 11
        return -1

    @staticmethod
    def store(data: list) -> list:
        hash_data = [0] * 11
        for d in data:
            k = Hashing._hash(d)
            if hash_data[k] != 0:
                k = (k + 1) % 11
            hash_data[k] = d
        return hash_data

    @staticmethod
    def _hash(value: int) -> int:
        return value % 11
