from sys import stdin
from collections import deque


class MazeExplorer(object):

    di = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    def __init__(self, n, m, mp):
        self._n = n
        self._m = m
        self._mp = mp
        self._visited = [[False]*m for _ in range(n)]
        self._queue = deque()

    def is_valid_point(self, x, y):
        if x < 0 or x >= self._n:
            return False
        if y < 0 or y >= self._m:
            return False
        if self._mp[x][y] == '0':
            return False
        if self._visited[x][y]:
            return False
        return True
        
    def break_out(self):
        self._queue.append((0, 0, 0))
        di = MazeExplorer.di
        while len(self._queue) != 0:
            cp = self._queue.popleft()
            if cp[0] == self._n-1 and cp[1] == self._m-1:
                break
            if self._visited[cp[0]][cp[1]]:
                continue

            self._visited[cp[0]][cp[1]] = True
            for i in range(4):
                np = (cp[0] + di[i][0],
                      cp[1] + di[i][1],
                      cp[2] + 1)
                if self.is_valid_point(np[0], np[1]):
                    self._queue.append(np)

        return cp[2]+1


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    mp = [list(stdin.readline()) for _ in range(n)]
    me = MazeExplorer(n, m, mp)
    print(me.break_out())
                
        
