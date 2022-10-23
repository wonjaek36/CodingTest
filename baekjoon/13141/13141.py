from sys import stdin
from math import inf


class Ignition(object):

    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        self.edges = edges
        self._mp = [
            [inf] * (self.n+1) for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            self._mp[i][i] = 0
        for x, y, v in self.edges:
            self._mp[x][y] = min(self._mp[x][y], v)
            self._mp[y][x] = min(self._mp[x][y], v)

    def _floyd(self):
        for k in range(1, self.n+1):
            for i in range(1, self.n+1):
                for j in range(1, self.n+1):
                    if self._mp[i][j] > self._mp[i][k] + self._mp[k][j]:
                        self._mp[i][j] = self._mp[i][k] + self._mp[k][j]

    def get_time(self, center):
        set_fire_times = [0] * (self.n+1)
        for i in range(1, self.n+1):
            set_fire_times[i] = self._mp[center][i]

        max_burn_time = -inf
        for x, y, v in edges:
            xf, yf = set_fire_times[x], set_fire_times[y]
            burn_time = (xf + yf + v) / 2
            max_burn_time = max(max_burn_time, burn_time)

        return max_burn_time

    def get_fire_time(self):
        self._floyd()

        min_time = inf
        for i in range(1, self.n+1):
            min_time = min(self.get_time(i), min_time)
        return min_time
            

if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    edges = [tuple(map(int, rd().split()))
             for _ in range(m)]
    ig = Ignition(n, m, edges)
    print('{:.1f}'.format(ig.get_fire_time()))
