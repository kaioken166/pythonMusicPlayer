class MyArray:
    def __init__(self, arr):
        self.arr = arr

    def getsum(self):
        return sum(self.arr)

    def getmin(self):
        return min(self.arr)

    def getmax(self):
        return max(self.arr)

    def getpairs(self):
        n = len(self.arr)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i] + self.arr[j] == 0:
                    res.append((self.arr[i], self.arr[j]))
        return res


arr = MyArray([1, 1, 1, 1, 1])
print(str(arr.getsum()))
