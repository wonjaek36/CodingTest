from collections import deque
import sys
from sys import stdin


class HideAndSeek(object):

    def __init__(self, n, k):
        self._n = n
        self._k = k
        self._visited = [False for _ in range(100001)]

    def _move(self, x, c):
        nexts = []
        if x-1 >= 0 and not self._visited[x-1]:
            self._visited[x-1] = True
            nexts.append((x-1, c+1))
        if x+1 <= 100000 and not self._visited[x+1]:
            self._visited[x+1] = True
            nexts.append((x+1, c+1))
        if x*2 <= 100000 and not self._visited[x*2]:
            self._visited[x*2] = True
            nexts.append((x*2, c+1))
            
        return nexts
        
    def seek(self):
        q = deque([(self._n, 0)])

        while len(q) != 0:
            x, c = q.popleft()
            if x == self._k:
                return c

            q.extend(self._move(x, c))
        return -1


if __name__ == '__main__':
    n, k = map(int, stdin.readline().rstrip().split(' '))
    
    has = HideAndSeek(n, k)
    print(has.seek())
