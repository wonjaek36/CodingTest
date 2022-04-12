import sys
from sys import stdin
sys.setrecursionlimit(10**6)


class SpanningTree(object):

    def __init__(self, v, edges):
        self._v = v
        self._edges = edges
        self._parent = [i for i in range(v+1)]

    def _union(self, a, b):
        p_a = self._find(a)
        p_b = self._find(b)
        self._parent[p_b] = p_a

    def _find(self, a):
        if self._parent[a] == a:
            return a
        self._parent[a] = self._find(self._parent[a])
        return self._parent[a]

    def get_weight(self):
        self._edges = sorted(self._edges, key=lambda x: x[2])
        weight = 0
        for edge in self._edges:
            p, q, v = edge
            pp = self._find(p)
            pq = self._find(q)

            if pp == pq:
                continue

            weight += v
            self._union(p, q)
        return weight


if __name__ == '__main__':
    v, e = list(map(
        int, stdin.readline().split(' ')))
    edges = []
    for i in range(e):
        edges.append(tuple(map(
            int, stdin.readline().split(' '))))
                    
    st = SpanningTree(v, edges)
    print(st.get_weight())
