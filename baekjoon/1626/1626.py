from sys import stdin


class SecondMst(object):
    
    def __init__(self, n: int, edges: list):
        self._n = n
        self._edges = edges
        self._group = [i for i in range(n+1)]
        self._adj = {i: [] for i in range(n+1)}
        self._parent = [(0, 0) for _ in range(n+1)]

    def get_weight(self):
        w = self._get_first_mst()
        return self._get_second_mst(w)

    def _get_first_mst(self):
        self._edges = sorted(self._edges, key=lambda x: x[2])
        weight = 0
        connected = 0
        for idx, e in enumerate(self._edges):
            pa, pb = self._find(e[0]), self._find(e[1])
            if pa == pb:
                continue
            
            self._union(pa, pb)
            self._adj[e[0]].append((e[1], e[2]))
            self._adj[e[1]].append((e[0], e[2]))
            weight += e[2]
            self._edges[idx][3] = True
            connected += 1
            if connected >= self._n-1:
                break
        return weight

    def _get_second_mst(self, mst_weight):
        self._create_mst_tree(1, -1, 0)
        min_weight = 0x7ffffff
        for e in self._edges:
            if e[3]:
                continue

            t, g, v, _ = e
            sv = self._get_max_edge_in_mst(t, g)

            if v == sv:
                continue
            min_weight = min(min_weight, mst_weight - sv + v)

        return min_weight

    def _get_max_edge_in_mst(self, a, b):
        ancestors = [False for _ in range(self._n+1)]
        p = a
        max_weight = 0
        while p != -1:
            max_weight = max(max_weight, self._parent[p][1])
            ancestors[p] = True
            p = self._parent[p][0]

        p = b
        while not ancestors[p]:
            max_weight = max(max_weight, self._parent[p][1])
            p = self._parent[p][0]

        return max_weight
    
    def _union(self, a, b):
        pa = self._find(a)
        pb = self._find(b)
        self._group[pb] = pa

    def _find(self, a):
        if self._group[a] == a:
            return a
        self._group[a] = self._find(self._group[a])
        return self._group[a]

    def _create_mst_tree(self, nn, parent, weight):
        if self._parent[nn][0] != 0:
            return
        self._parent[nn] = (parent, weight)
        for nxt in self._adj[nn]:
            self._create_mst_tree(nxt[0], nn, nxt[1])


if __name__ == '__main__':
    n, m = list(map(
        int, stdin.readline().rstrip().split(' ')))
    edges = []
    for _ in range(m):
        edges.append(list(map(
            int, stdin.readline().split(' '))))
        edges[-1].append(False)
    sm = SecondMst(n, edges)
    print(sm.get_weight())
