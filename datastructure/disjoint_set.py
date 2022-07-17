class Set:
    def __init__(self,n):
        self.parents = [None for i in range(n)] #items parents
        self.ranks = [0 for i in range(n)] # storing parents height
    def makeSet(self, i):
        self.parents[i] = i
        self.ranks[i] = 1
    def Find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.Find(self.parents[i])
        return self.parents[i]

    def Union(self, u, v):
        u_parent = self.Find(u)
        v_parent = self.Find(v)
        if self.ranks[u_parent] > self.ranks[v_parent]:
            self.parents[v_parent] = u_parent
        else:
            self.parents[u_parent] = v_parent
            if self.ranks[u_parent] == self.ranks[v_parent]:
                self.ranks[u] += 1
def main(n, arr):
    set = Set(n)
    for i in arr:
        set.makeSet(i)
    set.Union(2, 10)
    set.Union(7, 5)
    set.Union(6, 1)
    set.Union(3, 4)
    set.Union(5, 11)
    set.Union(7, 8)
    set.Union(7, 3)
    set.Union(12, 2)
    set.Union(9, 6)
    print(sum(set.ranks))




if __name__ == '__main__':
    n = 13
    arr = [i for i in range(13)]
    main(n, arr)
