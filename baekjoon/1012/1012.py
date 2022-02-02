from sys import stdin
from collections import deque


class CabbageWarm(object):

    di = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self, m, n, cabbages):
        self._m = m
        self._n = n
        self._cabbages = cabbages
        self._mp = [[0]*n for _ in range(m)]
        self._visited = [[False]*n for _ in range(m)]
        self._queue = None

    def _draw_map(self):
        for p in self._cabbages:
            self._mp[p[0]][p[1]] = 1

    def _is_valid(self, x, y):
        if x < 0 or x >= m:
            return False
        if y < 0 or y >= n:
            return False
        if self._visited[x][y]:
            return False
        if self._mp[x][y] == 0:
            return False
        return True
        
    def _fill_warm_area(self, x, y):
        self._queue = deque()
        self._queue.append((x, y))

        di = CabbageWarm.di
        while len(self._queue) != 0:
            pw = self._queue.popleft()

            if self._visited[pw[0]][pw[1]]:
                continue
            self._visited[pw[0]][pw[1]] = True

            for ix, iy in di:
                nw = (pw[0]+ix, pw[1]+iy)
                if self._is_valid(nw[0], nw[1]):
                    self._queue.append(nw)
        
    def count_need_warms(self):
        count = 0
        self._draw_map()
        for i in range(self._m):
            for j in range(self._n):
                if not self._visited[i][j] and\
                   self._mp[i][j] == 1:
                    self._fill_warm_area(i, j)
                    count+=1

        return count
        

if __name__ == '__main__':
    t = int(stdin.readline())
    for _ in range(t):
        m, n, k = list(map(int,
                           stdin.readline().split(' ')))
        cabbages = [
            list(map(int, stdin.readline().split(' ')))
            for _ in range(k)]

        cw = CabbageWarm(m, n, cabbages)
        print(cw.count_need_warms())
