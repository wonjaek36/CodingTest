import sys
from sys import stdin
import heapq


class Watering(object):
    # Prim

    def __init__(self, connects):
        self._n = len(connects)
        self._connects = connects
        self._hp = []
        self._visited = [False for _ in range(self._n+1)]

    def watering_all(self):
        heapq.heappush(self._hp, (0, 0))
        # value, node
        weight = 0

        while len(self._hp) != 0:
            cur = heapq.heappop(self._hp)
            v, n = cur

            if self._visited[n]:
                continue
            self._visited[n] = True
            weight += v

            for i, v in enumerate(self._connects[n]):
                if self._visited[i]:
                    continue
                heapq.heappush(self._hp, (v, i))
        return weight


if __name__ == '__main__':
    n = int(stdin.readline())
    directs = [int(stdin.readline()) for _ in range(n)]
    indirects = [
        [0]+list(map(int, stdin.readline().split(' ')))
    for _ in range(n)]
    connects = [[0]*(n+1)]

    connects.extend(indirects)
    for i, v in enumerate(directs):
        connects[0][i+1] = connects[i+1][0] = v

    w = Watering(connects)
    print(w.watering_all())
