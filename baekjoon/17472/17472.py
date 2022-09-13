from sys import stdin
from collections import deque
from math import inf
import heapq


class CreateBridge(object):

    def __init__(self, n, m, mp):
        self.n = n
        self.m = m
        self.mp = mp

        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 0:
                    continue
                self.mp[i][j] = -1

    def _coloring_island(self, x, y, num, visited):
        dq = deque([(x, y)])
        while dq:
            x, y = dq.popleft()
            self.mp[x][y] = num

            for dx, dy in [[-1, 0], [1, 0],
                           [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= self.n:
                    continue
                if ny < 0 or ny >= self.m:
                    continue
                if visited[nx][ny]:
                    continue
                if self.mp[nx][ny] == 0:
                    continue
                visited[nx][ny] = True
                dq.append((nx, ny))

    def _get_island(self):
        visited = [[False]*self.m for _ in range(self.n)]
        count = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.mp[i][j] == 0:
                    continue
                if visited[i][j]:
                    continue
                count += 1
                self._coloring_island(i, j, count, visited)

        self.edges = [[inf]*(count+1) for _ in range(count+1)]

    def _try_connect(self, x, y, num, di):
        dx, dy = di
        px, py = x + dx, y + dy
        count = 0

        while px < self.n and py < self.m and self.mp[px][py] == 0:
            count += 1
            px, py = px + dx, py + dy

        if count < 2 or px >= self.n or py >= self.m:
            return

        src, tar = num, self.mp[px][py]
        if self.edges[src][tar] > count:
            self.edges[src][tar] = count
            self.edges[tar][src] = count

    def _create_edges(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.mp[i][j] == 0:
                    continue

                self._try_connect(i, j, self.mp[i][j], (1, 0))
                self._try_connect(i, j, self.mp[i][j], (0, 1))

    def _prim(self):
        h = [(0, 1)]
        mst = 0
        visited = [False] * len(self.edges)
        connected = 1

        while h:
            v, c = heapq.heappop(h)
            if visited[c]:
                continue
            visited[c] = True
            connected += 1

            mst += v
            for i, v in enumerate(self.edges[c]):
                if visited[i] or v == inf:
                    continue
                heapq.heappush(h, (v, i))
        return mst if connected == len(self.edges) else -1

    def get_mst(self):
        self._get_island()
        self._create_edges()
        return self._prim()


if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    mp = [list(map(int, rd().split())) for _ in range(n)]

    cb = CreateBridge(n, m, mp)
    print(cb.get_mst())
