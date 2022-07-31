from sys import stdin
from collections import deque


class SafeArea(object):

    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.visited = None

    def valid_xy(self, x, y):
        return x >= 0 and x < self.n and\
            y >= 0 and y < self.n

    def check_unwatered_area(self, x, y, water_level):
        dq = deque()
        dq.append((x, y))
        assert self.visited is not None
        self.visited[x][y] = True
        while len(dq) != 0:
            cur = dq.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = cur[0] + dx
                ny = cur[1] + dy

                if not self.valid_xy(nx, ny):
                    continue
                if self.visited[nx][ny]:
                    continue
                if self.arr[nx][ny] <= water_level:
                    continue

                self.visited[nx][ny] = True
                dq.append((nx, ny))


    def get_safe_area(self, water_level):
        count = 0

        for i in range(self.n):
            for j in range(self.n):
                assert self.visited is not None
                if self.arr[i][j] > water_level and not self.visited[i][j]:
                    self.check_unwatered_area(i, j, water_level)
                    count += 1
        return count

    def get_max_safe_area(self):
        min_wl = min(map(min, self.arr))-1
        max_wl = max(map(max, self.arr))
        max_count = 0

        for water_level in range(min_wl, max_wl+1):
            self.visited = [[False]*self.n for _ in range(self.n)]
            cnt = self.get_safe_area(water_level)
            max_count = max(cnt, max_count)

        return max_count

if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    arr = [list(map(int, rd().split()))
           for _ in range(n)]
    sa = SafeArea(n, arr)
    print(sa.get_max_safe_area())
