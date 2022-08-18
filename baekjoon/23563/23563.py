from sys import stdin
import heapq


class Luciu(object):

    def __init__(self, n, m, mp):
        self.n = n
        self.m = m
        self.mp = mp
        self.visited = [
            [False for _ in range(m)]
            for _ in range(n)]
        self.is_closest_wall = [
            [False for _ in range(m)]
            for _ in range(n)]

    def _get_start_point(self):
        for i in range(n):
            for j in range(m):
                if self.mp[i][j] == 'S':
                    return (i, j)
        raise ValueError('No S in mp')

    def _is_touched_walled(self, x, y):
        if self.mp[x][y] == '#':
            return False

        for dx, dy in [[-1, 0], [1, 0],
                       [0, -1], [0, 1]]:
            cx = x + dx 
            cy = y + dy
            if cx < 0 or cx >= self.n:
                continue
            if cy < 0 or cy >= self.m:
                continue
            if self.mp[cx][cy] == '#':
                return True
        return False

    def _check_cloest_wall(self):
        for i in range(self.n):
            for j in range(self.m):
                if self._is_touched_walled(i, j):
                    self.is_closest_wall[i][j] = True

    def get_shortest_time(self):
        h = []
        sx, sy = self._get_start_point()
        h = [(0, sx, sy)]

        self._check_cloest_wall()
        while h:
            top = heapq.heappop(h)
            step, x, y = top
            if self.mp[x][y] == 'E':
                return step

            if self.visited[x][y]:
                continue
            self.visited[x][y] = True

            for dx, dy in [[-1, 0], [1, 0],
                           [0, -1], [0, 1]]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= self.n:
                    continue
                if ny < 0 or ny >= self.m:
                    continue
                if self.mp[nx][ny] == '#':
                    continue

                s = step
                if not (self.is_closest_wall[x][y] and
                        self.is_closest_wall[nx][ny]):
                    s = step + 1

                assert type(h) is list
                heapq.heappush(h, (s, nx, ny))

        raise ValueError('Fail to find E')


if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    mp = [rd().rstrip() for i in range(n)]

    l = Luciu(n, m, mp)
    print(l.get_shortest_time())
