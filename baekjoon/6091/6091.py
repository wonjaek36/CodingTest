from io import StringIO
from sys import stdin
import heapq
import io


class PinkFloyd(object):

    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def _put_edges(self, h, sr, edges, visited):
        for nxt, val in enumerate(edges):
            if visited[nxt]:
                continue
            heapq.heappush(h, (val, nxt, sr))
        return h

    def _prim(self):
        h = [(0, 0, 0)]
        visited = [False for _ in range(self.n)]
        connected = 0
        connects = []

        while h and connected < self.n:
            _, tg, sr = heapq.heappop(h)
            if visited[tg]:
                continue
            visited[tg] = True

            connects.append((sr, tg))
            connected += 1
            h = self._put_edges(h, tg, self.edges[tg], visited)

        edges = {_: [] for _ in range(self.n)}
        for x, y in connects[1:]:
            edges[x].append(y)
            edges[y].append(x)

        return edges

    def get_trees(self):
        ll = self._prim()
        strIo = io.StringIO()
        for i in range(self.n):
            strIo.write(str(len(ll[i])))
            for t in sorted(ll[i]):
                strIo.write(" "+str(t+1))
            strIo.write('\n')
        return strIo.getvalue()

if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    edges = [[0]*n for _ in range(n)]
    for i in range(n-1):
        for idx, j in enumerate(
                list(map(int, rd().split()))):
            edges[i][idx+i+1] = j
            edges[idx+i+1][i] = j

    pf = PinkFloyd(n, edges)
    print(pf.get_trees())
