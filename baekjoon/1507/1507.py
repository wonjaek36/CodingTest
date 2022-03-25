import sys
from sys import stdin


class CuriousMinho(object):

    def __init__(self, n, graph):
        self._n = n
        self._graph = graph
        self._edges = [[1]*n for _ in range(n)]
        self._invalid_graph = False
        for i in range(n):
            self._edges[i][i] = 0
        

    def eliminate_unness_edges(self):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == k or k == j:
                        continue
                    if self._graph[i][j] == (
                            self._graph[i][k] + self._graph[k][j]):
                        self._edges[i][j] = 0

                    if self._graph[i][j] > (
                            self._graph[i][k] + self._graph[k][j]):
                        self._invalid_graph =True

    def sum_edges(self):
        if self._invalid_graph:
            return -1
        
        s = 0
        for i in range(n):
            for j in range(i, n):
                if self._edges[i][j] == 1:
                    s += self._graph[i][j]
        return s
    

if __name__ == '__main__':
    n = int(stdin.readline())
    graph = []
    for _ in range(n):
        row = list(map(
            int, stdin.readline().split(' ')))
        graph.append(row)

    cm = CuriousMinho(n, graph)
    cm.eliminate_unness_edges()
    print(cm.sum_edges())
    
