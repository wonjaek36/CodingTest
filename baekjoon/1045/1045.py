from sys import stdin
from collections import Counter


class Road(object):

    def __init__(self, n, m, mp):
        self.n = n
        self.m = m
        self.mp = mp
        self.parents = [_ for _ in range(n)]

    def _union(self, a, b):
        pa = self._find(a)
        pb = self._find(b)

        self.parents[pb] = pa

    def _find(self, a):
        if self.parents[a] == a:
            return a
        self.parents[a] = self._find(self.parents[a])
        return self.parents[a]

    def get_connections(self):
        connects = []
        for i in range(self.n):
            for j in range(self.n):
                if mp[i][j] == 'N':
                    continue
                if self._find(i) == self._find(j):
                    continue

                self.mp[i][j] = self.mp[j][i] = 'C'
                self._union(i, j)
                connects.append(i)
                connects.append(j)
        if len(connects) != (self.n-1)*2:
            return [-1]

        for i in range(self.n):
            for j in range(self.n):
                if len(connects) >= self.m*2:
                    continue
                if mp[i][j] == 'Y':
                    self.mp[i][j] = self.mp[j][i] = 'C'
                    connects.append(i)
                    connects.append(j)

        if len(connects) != self.m*2:
            return [-1]

        if self.n == 1:
            return [0]

        return list(map(lambda x: x[1],
                   sorted(Counter(connects).items(), key=lambda x: x[0])))

if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    mp = [list(rd().rstrip()) for _ in range(n)]
    r = Road(n, m, mp)
    print(*r.get_connections())
