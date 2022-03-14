import sys
from sys import stdin
from queue import PriorityQueue


class ShortestPath(object):

    def __init__(self, v, s, edges):
        self._v = v
        self._s = s
        self._edges = edges
        self._visited = [-1 for _ in range(v+1)]

    def get_shortest_path_to_all(self):
        que = PriorityQueue()

        que.put((0, self._s))
        while not que.empty():
            v, n = que.get()

            if self._visited[n] != -1:
                continue

            self._visited[n] = v

            for edge in self._edges[n]:
                que.put((v+edge[1], edge[0]))

        return self.format_visited()

    def format_visited(self):
        return list(
            map(lambda x: 'INF' if x == -1 else x,
                self._visited[1:]))


if __name__ == '__main__':
    v, e = list(
        map(int, stdin.readline().rstrip().split(' ')))
    s = int(stdin.readline().rstrip())
    edges = {i: [] for i in range(1, v+1)}
    for _ in range(e):
        x, y, w = list(
            map(int, stdin.readline().rstrip().split(' ')))
        edges[x].append((y, w))

    sp = ShortestPath(v, s, edges)
    nodes = sp.get_shortest_path_to_all()
    print('\n'.join(
        map(str, nodes)))
