import sys
from sys import stdin
from queue import PriorityQueue


class MakeMaze(object):

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def __init__(self, n, mp):
        self._n = n
        self._mp = mp
        self._visited = [[False]*n for _ in range(n)]

    def _is_valid(self, x, y):
        if x < 0 or x >= n:
            return False
        if y < 0 or y >= n:
            return False
        if self._visited[x][y]:
            return False

        return True
    
    def _next_moves(self, c):
        moves = []
        for dx, dy in MakeMaze.directions:
            x = dx + c[1]
            y = dy + c[2]
            d = c[0]
            if not self._is_valid(x, y):
                continue

            if self._mp[x][y] == '0':
                d += 1

            moves.append((d, x, y))
        return moves
        
    def search(self):
        q = PriorityQueue()

        q.put((0, 0, 0), block=False)
        while not q.empty():
            c = q.get(block=False)
            if c[1] == n-1 and c[2] == n-1:
                break
            if self._visited[c[1]][c[2]]:
                continue
            
            self._visited[c[1]][c[2]] = True
            nxts = self._next_moves(c)
            for nxt in nxts:
                q.put(nxt, block=False)

        return c[0]

    
if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    mp = [list(stdin.readline().rstrip()) for _ in range(n)]

    mm = MakeMaze(n, mp)
    print(mm.search())
