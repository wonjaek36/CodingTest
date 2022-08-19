from sys import stdin
from collections import deque


class KevinBacon(object):

    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        self.edges = edges

    def _get_kevin_bacon_num(self, s):
        d = deque([(s, 0)])
        self.visited = [-1 for _ in range(self.n+1)]
        self.visited[0], self.visited[s] = 0, 0

        while d:
            cur, step = d.popleft()
            for edge in edges:
                if edge[0] != cur and edge[1] != cur:
                    continue
            
                if edge[0] == cur:
                    nxt = edge[1]
                else:
                    nxt = edge[0]

                if self.visited[nxt] != -1:
                    continue
                self.visited[nxt] = step+1
                d.append((nxt, step+1))

        return sum(self.visited)

    def get_num_smallest_kb(self):
        min_kb_num = (0x7fffffff, -1)

        for i in range(1, self.n+1):
            kb_num = self._get_kevin_bacon_num(i)
            min_kb_num = min(
                min_kb_num, (kb_num, i), key=lambda x: x[0])

        return min_kb_num[1]


if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    edges = [tuple(map(int, rd().split()))
             for _ in range(m)]
    
    kb = KevinBacon(n, m, edges)
    print(kb.get_num_smallest_kb())
