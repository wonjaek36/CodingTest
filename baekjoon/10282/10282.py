import sys
from sys import stdin
from queue import PriorityQueue


class HackingTime(object):

    def __init__(self, n, c, edges):
        self._n = n
        self._c = c
        self._edges = edges
        self._visited = [-1 for _ in range(self._n+1)]

    def spread_virus(self):
        que = PriorityQueue()

        que.put((0, self._c))
        while not que.empty():
            v, n = que.get()

            if self._visited[n] != -1:
                continue

            self._visited[n] = v
            for edge in self._edges[n]:
                que.put((v+edge[1], edge[0]))

        return len(
            list(filter(
                lambda x: x != -1,
                self._visited))), max(self._visited)
        
        

if __name__ == '__main__':
    T = int(stdin.readline().rstrip())
    for _ in range(T):
        n, d, c = list(
            map(int, stdin.readline().rstrip().split(' ')))

        edges = {i:[] for i in range(1, n+1)}
        for _ in range(d):
            x, y, v = list(
                map(int, stdin.readline().rstrip().split(' ')))
            edges[y].append((x, v))

        ht = HackingTime(n, c, edges)
        c, t = ht.spread_virus()
        print(c, t)
        
            
