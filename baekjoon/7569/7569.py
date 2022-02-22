from collections import deque
import sys
from sys import stdin


class TomatoBox(object):

    directions = [
        [0, 0, -1], [0, 0, 1],
        [0, -1, 0], [0, 1, 0],
        [-1, 0, 0], [1, 0, 0]]
    
    def __init__(self, h, n, m, mp):
        self._h = h
        self._n = n
        self._m = m
        self._mp = mp

    def _get_ripen_tomatos(self):
        ripens = []
        for k in range(self._h):
            for i in range(self._n):
                for j in range(self._m):
                    if self._mp[k][i][j] == 1:
                        ripens.append((k, i, j, 0))

        return ripens

    def _is_valid(self, p):
        z, x, y = p
        if z < 0 or z >= self._h:
            return False
        if x < 0 or x >= self._n:
            return False
        if y < 0 or y >= self._m:
            return False
        if self._mp[z][x][y] == -1 or self._mp[z][x][y] == 1:
            return False

        return True
        
    def _next_moves(self, cur):
        directions = TomatoBox.directions
        cz, cx, cy, cc = cur
        moves = []
        for dz, dx, dy in directions:
            nz = dz + cz
            nx = dx + cx
            ny = dy + cy

            if not self._is_valid((nz, nx, ny)):
                continue

            self._mp[nz][nx][ny] = 1
            moves.append((nz, nx, ny, cc+1))

        return moves
                    
    def get_ripen_day(self):
        ripens = self._get_ripen_tomatos()
        q = deque()
        q.extend(ripens)
        max_count = 0
        while len(q) != 0:
            cur = q.popleft()
            max_count = max(max_count, cur[-1])
            moves = self._next_moves(cur)

            q.extend(moves)
        
        for hi in range(self._h):
            for ni in range(self._n):
                if len(list(filter(lambda x: x == 0, self._mp[hi][ni]))) != 0:
                   return -1
        
        return max_count
    
        
if __name__ == '__main__':
    m, n, h = list(
        map(int, stdin.readline().rstrip().split(' ')))
    mp = []

    for _ in range(h):
        floor = []
        for _ in range(n):
            floor.append(
                list(map(int, stdin.readline().rstrip().split(' '))))
        mp.append(floor)

    tb = TomatoBox(h, n, m, mp)
    print(tb.get_ripen_day())
