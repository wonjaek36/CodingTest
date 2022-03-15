import sys
from sys import stdin


class Exercise(object):

    def __init__(self, n, path):
        self._n = n
        self._path = path

    def compute_all_path(self):
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if self._path[i][j] >\
                       self._path[i][k]+self._path[k][j]:
                        self._path[i][j] =\
                            self._path[i][k]+self._path[k][j]

    def get_min_cycle(self):
        min_cycle = 400000000
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                min_cycle = min(
                    min_cycle, self._path[i][j]+self._path[j][i])
        return min_cycle if min_cycle < 400000000 else -1

    
if __name__ == '__main__':
    n, m = list(
        map(int, stdin.readline().rstrip().split(' ')))

    path = [[4000000000]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y, v = list(
            map(int, stdin.readline().rstrip().split(' ')))
        path[x][y] = v
    for i in range(1, n):
        path[i][i] = 0

    ex = Exercise(n, path)
    ex.compute_all_path()
    print(ex.get_min_cycle())
    
