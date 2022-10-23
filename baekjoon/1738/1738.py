from sys import stdin
from math import inf


class Alley(object):

    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        self.edges = edges
        self.visited = [-inf for _ in range(n+1)]
        self.visited[1] = 0
        self.froms = [-1 for _ in range(n+1)]

    def get_best_path(self):
        for _ in range(self.n-1):
            for x, y, v in self.edges:
                if self.visited[x] + v > self.visited[y]:
                    self.visited[y] = self.visited[x] + v
                    self.froms[y] = x

        for idx, (x, y, v) in enumerate(self.edges):
            if self.visited[x] + v > self.visited[y]:
                self.edges[idx] = (x, y, inf)
                self.visited[y] = self.visited[x] + inf 
                self.froms[y] = x

        pos = self.n
        paths = []
        while pos != -1:
            if pos in paths:
                return [-1]
            paths.append(pos)
            pos = self.froms[pos]

        return paths[::-1]


if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    edges = [
        tuple(map(int, rd().split())) for _ in range(m)]
    a = Alley(n, m, edges)
    path = a.get_best_path()
    
    print(' '.join(map(str, path)))

