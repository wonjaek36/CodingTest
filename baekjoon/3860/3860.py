import sys
from sys import stdin
import pprint

class HalloweenGrave(object):

    INF = 1e8+7
    di = [[-1, 0],
          [ 1, 0],
          [ 0,-1],
          [ 0, 1]]
    
    def __init__(self, w, h, graves, holes):
        self._w = w
        self._h = h
        self._graves = graves
        self._holes = holes
        self._nodes = [[0]*self._h for _ in range(self._w)]
        self._edges = []
        self._map = [[0]*self._h for _ in range(self._w)]

    def draw_map(self):
        self._edges.extend(self._holes)
        for x, y in self._graves:
            self._map[x][y] = 1
        for x, y, _, _, _ in self._holes:
            self._map[x][y] = 2
        
        for i in range(self._w):
            for j in range(self._h):
                self._nodes[i][j] = self.INF
                if i == self._w-1 and j == self._h-1:
                    continue
                if self._map[i][j] != 0:
                    continue
                
                self._edges.extend(self._create_edges(i, j))
                
        self._nodes[0][0] = 0

    def _create_edges(self, x, y):
        def is_valid(p):
            _, _, x, y, _ = p
            return (x >= 0 and y >= 0) and\
                (x < self._w and y < self._h) and\
                (self._map[x][y] != 1)
        
        c = [(x, y, x+dx, y+dy, 1) for dx, dy in self.di]
        return list(filter(lambda x: is_valid(x), c))

    def search(self):
        pprint.pprint(self._map)
        pprint.pprint(self._edges)
        for _ in range(self._w*self._h-1):
            for edge in self._edges:
                cx, cy, nx, ny, v = edge
                if self._nodes[cx][cy] == self.INF:
                    continue

                cv = self._nodes[cx][cy]
                nv = self._nodes[nx][ny]
                if cv + v < nv:
                    self._nodes[nx][ny] = cv + v

        pprint.pprint(self._nodes)
        for edge in self._edges:
            cx, cy, nx, ny, v = edge
            if self._nodes[cx][cy] == self.INF:
                continue

            cv = self._nodes[cx][cy]
            nv = self._nodes[nx][ny]
            if cv + v < nv:
                return 'Never'

        dv = self._nodes[self._w-1][self._h-1]
        if dv == self.INF:
           return 'Impossible'

        return dv

    
if __name__ == '__main__':
    while True:
        w, h = stdin.readline().split(' ')
        w, h = int(w), int(h)
        if w == 0 and h == 0:
            break
        g = int(stdin.readline())
        graves = set([
            tuple(map(
                int, stdin.readline().split(' ')))
            for _ in range(g)])
        e = int(stdin.readline())
        holes = [
            tuple(map(
                int, stdin.readline().split(' ')))
            for _ in  range(e)]

        hg = HalloweenGrave(w, h, graves, holes)
        hg.draw_map()
        print(hg.search())
