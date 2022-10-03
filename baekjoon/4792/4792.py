from sys import stdin


class RedBlueST(object):

    def __init__(self, n, m, k, edges):
        self.n = n
        self.m = m
        self.k = k
        self.edges = edges
        self.parents = []

    def _union(self, a, b):
        pa = self._find(a) 
        pb = self._find(b)
        self.parents[pb] = pa

    def _find(self, a):
        if self.parents[a] == a:
            return a
        self.parents[a] = self._find(self.parents[a])
        return self.parents[a]

    def _get_blues(self, blue=True):
        edges = sorted(self.edges, key=lambda x: x[0], reverse=not blue)
        self.parents = [_ for _ in range(self.n+1)]

        blues = 0
        connects = 0
        for c, x, y in edges:
            x, y = int(x), int(y)
            if self._find(x) == self._find(y):
                continue

            self._union(x, y)
            connects += 1
            blues += 1 if c == 'B' else 0

        return blues if connects == self.n-1 else -1

    def is_possible(self):
        max_b = self._get_blues(blue=True)
        min_b = self._get_blues(blue=False)

        if max_b == -1 or min_b == -1:
            return 0
        return 1 if min_b <= k <= max_b else 0

if __name__ == '__main__':
    rd = stdin.readline
    while True:
        n, m, k = tuple(map(int, rd().split()))
        if n == 0 and m == 0 and k == 0:
            break

        edges = [list(rd().rstrip().split())
                 for _ in range(m)]
        rbst = RedBlueST(n, m, k, edges)
        print(rbst.is_possible())
