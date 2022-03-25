import sys
from sys import stdin
from queue import PriorityQueue


class SpecificShortestPath(object):

    INF = 1e7+7
    
    def __init__(self, n, edges, sn):
        self._n = n
        self._edges = edges
        self._sn = sn
        self._visited = {}
        self._nodes = [1]
        self._nodes.extend(sn)

    def _search_with_nodes(self, s):
        self._visited[s] = [self.INF]*(self._n+1)
        self._visited[s][s] = 0
        started = [False]*(self._n+1)
        
        q = PriorityQueue()
        q.put((0, s))
        
        while not q.empty():
            c = q.get()
            cv, n = c[0], c[1]  # current value, node

            if started[n]:
                continue
            started[n] = True

            for nn, ev in self._edges[n]:
                # next node, edge value
                if self._visited[s][nn] <= cv+ev:
                    continue

                self._visited[s][nn] = cv+ev
                q.put((cv+ev, nn))

        del q
        
    def search(self):
        for s in self._nodes:
            self._search_with_nodes(s)

        v = min(self._visited[1][sn[0]]+
                self._visited[sn[0]][sn[1]]+
                self._visited[sn[1]][self._n],
                # ---------
                self._visited[1][sn[1]]+
                self._visited[sn[1]][sn[0]]+
                self._visited[sn[0]][self._n])

        return v if v < self.INF else -1

    
if __name__ == '__main__':
    n, e = list(map(
        int, stdin.readline().split(' ')))
    edges = {i: [] for i in range(n+1)}
    for _ in range(e):
        a, b, c = list(map(
            int, stdin.readline().split(' ')))
        edges[a].append((b, c))
        edges[b].append((a, c))
    sn = list(map(
        int, stdin.readline().split(' ')))

    ssp = SpecificShortestPath(n ,edges, sn)
    print(ssp.search())
