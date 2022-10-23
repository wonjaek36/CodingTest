from sys import stdin
from collections import defaultdict
import heapq
from math import inf


class Pavement(object):

    def __init__(self, n, m, k, edges):
        self.n = n
        self.m = m
        self.k = k
        self.edges = edges
        self.visited = [[inf]*(n+1) for _ in range(k+1)]
        self.nton = defaultdict(list)
        for x, y, v in edges:
            self.nton[x].append((y, v))
            self.nton[y].append((x, v))

    def get_time(self):
        h = []
        heapq.heappush(h, (0, 0, 1))
        self.visited[0][1] = 0
        # distance, cpaved, loc

        while h:
            c = heapq.heappop(h)
            dis, cpaved, loc = c
            if self.visited[cpaved][loc] < dis:
                continue

            for nxt, nxt_dis in self.nton[loc]:
                if self.visited[cpaved][nxt] > nxt_dis + dis:
                    self.visited[cpaved][nxt] = nxt_dis + dis
                    heapq.heappush(h, (nxt_dis+dis,
                                       cpaved,
                                       nxt))

                if cpaved+1 <= k and\
                        self.visited[cpaved+1][nxt] > dis:
                    self.visited[cpaved+1][nxt] = dis
                    heapq.heappush(h, (dis,
                                       cpaved+1,
                                       nxt))
        return min(map(lambda x: x[-1], self.visited))


if __name__ == '__main__':
    rd = stdin.readline
    n, m, k = tuple(map(int, rd().split()))
    edges = [
        tuple(map(int, rd().split())) for _ in range(m)]

    p = Pavement(n, m, k, edges)
    print(p.get_time())
