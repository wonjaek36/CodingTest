import sys
from sys import stdin
sys.setrecursionlimit(10**6)


class Island(object):

    di = [[-1, -1], [-1, 0], [-1, 1],
          [ 0, -1],          [ 0, 1],
          [ 1, -1], [ 1, 0], [ 1, 1]]
    
    def __init__(self, w, h, mp):
        self._w = w
        self._h = h
        self._mp = mp
        self._visited = [[False]*w for _ in range(h)]

    def _is_land(self, x, y):
        if x < 0 or x >= self._h:
            return False
        if y < 0 or y >= self._w:
            return False
        if self._mp[x][y] == 0:
            return False
        return True
        
    def _mark_island(self, x, y):
        if self._visited[x][y]:
            return

        self._visited[x][y] = True
        for dx, dy in Island.di:
            nx = x + dx
            ny = y + dy
            
            if self._is_land(nx, ny):
                self._mark_island(nx, ny)
        
    def count_island(self):
        count = 0
        for i in range(self._h):
            for j in range(self._w):
                if self._mp[i][j] == 0 or self._visited[i][j]:
                    continue

                count += 1
                self._mark_island(i, j)

        return count


if __name__ == '__main__':
    while True:
        w, h = list(
            map(int, stdin.readline().split(' ')))
        if w == 0 and h == 0:
            break
        mp = [list(map(int, stdin.readline().split(' ')))
              for _ in range(h)]
                
        island = Island(w, h, mp)
        print(island.count_island())
