class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.arr[h] and self.arr[h][0] == key:
            self.arr[h] = (key, val)
            return

        while self.arr[h]:
            if h == self.MAX - 1:
                h = 0
            else:
                h += 1

        self.arr[h] = (key, val)


    def __getitem__(self, key):
        h = self.get_hash(key)

        while self.arr[h][0] != key:
            if h == self.MAX - 1:
                h = 0
            else:
                h += 1

        return self.arr[h][1]


if __name__ == "__main__" :
    ht = HashTable()

    ht['march 6'] = 120
    ht['march 6'] = 30
    ht['march 8'] = 67
    ht['march 9'] = 45
    ht['march 17'] = 459

    print(ht['march 6'])
