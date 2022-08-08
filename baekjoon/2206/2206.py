from sys import stdin
from collections import deque


class Destroyer(object):

    def __init__(self, n, m, mp):
        self.n = n
        self.m = m
        self.mp = mp
        self.visited = [
            [[-1, -1] for _ in range(m)] for _ in range(n)]

    def get_shortest_distance(self):
        dq = deque([(0, 0, 0, 0)])
        # x, y, d, step
        self.visited[0][0][0] = 0

        while len(dq) != 0:
            cur = dq.popleft()
            if cur[0] == self.n-1 and cur[1] == self.m-1:
                return cur[3]+1

            for dx, dy in [[-1, 0], [1, 0],
                      [0, -1], [0, 1]]:
                nx = cur[0] + dx
                ny = cur[1] + dy
                d = cur[2]

                if nx < 0 or nx >= self.n:
                    continue
                if ny < 0 or ny >= self.m:
                    continue
                if d == 1 and self.mp[nx][ny] == '1':
                    continue
                if self.mp[nx][ny] == '1':
                    d = 1
                if self.visited[nx][ny][d] != -1:
                    continue

                self.visited[nx][ny][d] = cur[3] + 1
                dq.append((nx, ny, d, cur[3]+1))

        return -1


if __name__ == '__main__':
    rd = stdin.readline
    n, m = map(int, rd().split())
    mp = [list(rd().strip()) for _ in range(n)]

    d = Destroyer(n, m, mp)
    print(d.get_shortest_distance())
