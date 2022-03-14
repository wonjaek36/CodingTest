import sys
from sys import stdin
sys.setrecursionlimit(10 ** 6)


class TimeMachine(object):

    INF = int(1e10+7)

    def __init__(self, n, edges):
        self._n = n
        self._edges = edges
        self._distance = [self.INF]*(n+1)
        self._distance[1] = 0

    def get_distance(self):
        for _ in range(self._n-1):
            for _a, _b, _c in edges:
                if self._distance[_a] == self.INF:
                    continue
                if self._distance[_a]+_c < self._distance[_b]:
                    self._distance[_b] = self._distance[_a] + _c

        for _a, _b, _c in edges:
            if self._distance[_a] == self.INF:
                continue
            if self._distance[_a] + _c < self._distance[_b]:
                return -1

        self._distance = list(
            map(lambda x: -1 if x == self.INF else x, self._distance))
        return '\n'.join(map(str, self._distance[2:]))


if __name__ == "__main__":
    n, m = list(map(
        int, stdin.readline().rstrip().split(' ')))
    edges = []
    for _ in range(m):
        a, b, c = list(map(
            int, stdin.readline().rstrip().split(' ')))
        edges.append((a, b, c))

    tm = TimeMachine(n, edges)
    print(tm.get_distance())
