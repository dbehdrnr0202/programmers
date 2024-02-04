
class DisjointSet:	
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n
    # union by size
    def find_size(self, a):
        parent = self.data[a]
        if parent < 0:
            return a
        return self.find_size(parent)
    def union_size(self, a, b):
        a, b = self.find_size(a), self.find_size(b)
        if a == b:
            return
        if self.data[a] < self.data[b]:
            self.data[a] += self.data[b]
            self.data[b] = a
        else:
            self.data[b] += self.data[a]
            self.data[a] = b
        self.size -= 1
    # union by rank
    def find_rank(self, idx):
        parent = self.data[idx]
        if parent < 0:
            return idx
        return self.find_rank(parent)
    def union_rank(self, x, y):
        x, y = self.find_rank(x), self.find_rank(y)
        if x == y:
            return
        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
        self.size -= 1
def test():
    a = DisjointSet(10)
    a.union_rank(0, 1)
    a.union_rank(2, 3)
    a.union_rank(1, 2)
    a.union_rank(0, 1)
    a.union_rank(4, 5)
    a.union_rank(5, 6)
    a.union_rank(7, 8)
    a.union_rank(7, 9)
    print(a.data)
    print(a.size)
    s = DisjointSet(10)
    s.union_size(0, 1)
    s.union_size(2, 3)
    s.union_size(1, 2)
    s.union_size(0, 1)
    s.union_size(4, 5)
    s.union_size(5, 6)
    s.union_size(7, 8)
    s.union_size(7, 9)
    print(s.data)
    print(s.size)
test()