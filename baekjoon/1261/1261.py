from sys import stdin
import heapq


class Algospot(object):

    def __init__(self, m, n, mp):
        self.m = m
        self.n = n
        self.mp = mp
        self.visited = [[False]*n for _ in range(m)]

    def get_minimum_destroy(self):
        hp = [(0, 0, 0)]

        while hp:
            d, x, y = heapq.heappop(hp)
            if self.visited[x][y]:
                continue

            if x == self.m-1 and y == self.n-1:
                return d

            self.visited[x][y] = True
            for dx, dy in [[-1, 0], [1, 0],
                           [0, -1], [0, 1]]:
                nx, ny, nd = x + dx, y + dy, d
                if nx < 0 or nx >= self.m:
                    continue
                if ny < 0 or ny >= self.n:
                    continue
                if self.visited[nx][ny]:
                    continue
                if self.mp[nx][ny] == 1:
                    nd += 1
                heapq.heappush(hp, (nd, nx, ny))


if __name__ == '__main__':
    rd = stdin.readline
    n, m = list(map(int, rd().split()))
    mp = [list(map(int, list(rd().strip())))
          for _ in range(m)]

    a = Algospot(m, n, mp)
    print(a.get_minimum_destroy())
