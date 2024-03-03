class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            value = ord(i)
            h += value
        return h % self.MAX


    def __setitem__(self, key, value):
        hash = self.get_hash(key)

        found = False
        for idx, el in enumerate(self.arr[hash]):
            if el[0] == key:
                self.arr[hash][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))


    def __getitem__(self, key):
        hash = self.get_hash(key)

        for idx, el in enumerate(self.arr[hash]):
            if el[0] == key:
                return el[1]


    def __delitem__(self, key):
        hash = self.get_hash(key)

        for idx, el in enumerate(self.arr[hash]):
            if el[0] == key:
                del self.arr[hash][idx]


if __name__ == "__main__" :
    ht = HashTable()

    ht['march 6'] = 120
    ht['march 6'] = 300
    ht['march 8'] = 67
    ht['march 9'] = 45
    ht['march 17'] = 459

    print(ht['march 6'])
