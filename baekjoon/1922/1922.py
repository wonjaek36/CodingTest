import sys
from sys import stdin
import heapq


class SpanningTree(object):

    def __init__(self, n, edges):
        self._n = n
        self._edges = edges
        self._heap = []
        self._visited = [False]*(n+1)
        self._group = 0

    def get_weight(self):
        weight = 0
        self._group = 1
        self._visited[1] = True
        for edge in self._edges[1]:
            heapq.heappush(self._heap, edge)
        
        while self._group != self._n:
            v, n = heapq.heappop(self._heap)
            if self._visited[n]:
                continue

            self._visited[n] = True
            weight += v
            self._group += 1
            for edge in self._edges[n]:
                heapq.heappush(self._heap, edge)
        return weight


if __name__ == '__main__':
    n = int(stdin.readline())
    m = int(stdin.readline())
    edges = {i: [] for i in range(n+1)}
    for _ in range(m):
        a, b, c = tuple(map(
            int, stdin.readline().split(' ')))
        edges[a].append((c, b))
        edges[b].append((c, a))

    st = SpanningTree(n, edges)
    print(st.get_weight())
