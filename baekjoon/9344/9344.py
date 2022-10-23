from sys import stdin
import heapq


class Road(object):

    def __init__(self, n, m, p, q, edges):
        self.n = n
        self.m = m
        self.p = p
        self.q = q
        self.edges = edges

    def _put_edges(self, h, edges, visited):
        for nxt, val in edges:
            if visited[nxt]:
                continue
            heapq.heappush(h, (val, nxt))
        return h

    def _prim(self):
        tv1, tv2, tval = list(
            filter(lambda x: ((x[0] == self.p and
                              x[1] == self.q) or
                              (x[0] == self.q and
                               x[1] == self.p)),
                   self.edges))[-1]
        mst = tval
        h = []
        visited = [False for _ in range(self.n+1)]
        visited[tv1] = True
        visited[tv2] = True
        connected = 1
        edges = {_: [] for _ in range(self.n+1)}
        for x, y, v in self.edges:
            if x == tv1 and y == tv2:
                continue
            edges[x].append((y, v))
            edges[y].append((x, v))

        h = self._put_edges(h, edges[tv1], visited)
        h = self._put_edges(h, edges[tv2], visited)

        while h and connected < self.n-1:
            val, tg = heapq.heappop(h)
            if visited[tg]:
                continue
            visited[tg] = True

            mst += val
            connected += 1
            h = self._put_edges(h, edges[tg], visited)
        return mst

    def _union(self, x, y):
        px = self._find(x)
        py = self._find(y)

        self.parents[py] = px

    def _find(self, x):
        if self.parents[x] == x:
            return x

        self.parents[x] = self._find(self.parents[x])
        return self.parents[x]

    def _kruskal(self):
        edges = list(self.edges)
        edges = sorted(edges, key=lambda x: x[2])
        self.parents = [_ for _ in range(self.n+1)]
        p, connected = 0, 0
        mst = 0
        while connected < self.n-1 and p < self.m:
            x, y, v = edges[p]
            p += 1

            px = self._find(x)
            py = self._find(y)
            if px == py:
                continue
            self._union(x, y)
            mst += v

        return mst
        
    def get_possible(self):
        kruskal_mst = self._kruskal()
        prim_mst = self._prim()

        return "YES" if kruskal_mst == prim_mst else "NO"

if __name__ == '__main__':
    rd = stdin.readline
    T = int(rd())
    for _ in range(T):
        n, m, p, q = tuple(map(int, rd().split()))
        assert type(m) is int
        edges = [
            tuple(map(int, rd().split())) for _ in range(m)]

        r = Road(n, m, p, q, edges)
        print(r.get_possible())
