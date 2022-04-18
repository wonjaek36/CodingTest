import sys
from sys import stdin


class TwoTown(object):

    def __init__(self, n, edges):
        self._n = n
        self._edges = edges
        self._parent = [i for i in range(n+1)]

    def get_weight(self):
        edges = sorted(self._edges, key=lambda x: x[2])
        weight = 0
        connected = 0
        for e in edges:
            a = self._find(e[0])
            b = self._find(e[1])
            if a == b:
                continue
            self._union(a, b)
            weight += e[2]
            connected += 1
            if connected >= n-2:
                break

        return weight

    def _union(self, a, b):
        pa = self._find(a)
        pb = self._find(b)

        self._parent[pb] = pa

    def _find(self, a):
        if self._parent[a] == a:
            return a

        self._parent[a] = self._find(self._parent[a])
        return self._parent[a]
        

if __name__ == '__main__':
    n, m = list(map(int,
                    stdin.readline().split(' ')))
    edges = []
    for _ in range(m):
        edges.append(tuple(
            map(int, stdin.readline().split(' '))))
    tt = TwoTown(n, edges)
    print(tt.get_weight())
