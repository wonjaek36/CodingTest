from sys import stdin
import sys
sys.setrecursionlimit(10**6)


class ConnectedComponent(object):

    def __init__(self, n, edges):
        self._n = n
        self._edges = edges
        self._visited = [False for _ in range(n+1)]

    def _search_nodes(self, p):
        if self._visited[p]:
            return

        self._visited[p] = True
        for i in self._edges[p]:
            self._search_nodes(i)
        
    def count_components(self):
        count = 0
        for i in range(1, self._n+1):
            if self._visited[i]:
                continue

            self._search_nodes(i)
            count += 1

        return count

    
if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split(' ')))
    edges = [set() for _ in range(n+1)]
    for _ in range(m):
        a, b = list(
            map(int, stdin.readline().split(' ')))
        edges[a].add(b)
        edges[b].add(a)

    cc = ConnectedComponent(n, edges)
    print(cc.count_components())
