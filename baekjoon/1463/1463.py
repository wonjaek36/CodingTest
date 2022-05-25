import sys
from sys import stdin
sys.setrecursionlimit(10**8)


class MakingOne(object):

    def __init__(self, n):
        self.n = n
        self._visited = [-1 for _ in range(n+1)]
        self._visited[0] = 0x7fffffff
        self._visited[1] = 0

    def _get_min_value(self, i):
        val = 0x7fffffff
        if i % 3 == 0:
            val = min(val, self._visited[i // 3])
        if i % 2 == 0:
            val = min(val, self._visited[i // 2])
        val = min(val, self._visited[i-1])
        return val + 1

    def count(self):
        for i in range(2, self.n+1):
            self._visited[i] = self._get_min_value(i)
        return self._visited[self.n]


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    mo = MakingOne(n)
    print(mo.count())
