from collections import deque
import sys
from sys import stdin


class TomatoBox(object):

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def __init__(self, n, m, box):
        self._n = n
        self._m = m
        self._box = box

    def _get_initial_ripen_tomato(self):
        tomatos = []
        for i in range(self._m):
            for j in range(self._n):
                if self._box[i][j] == 1:
                    tomatos.append((i, j, 0))

        return tomatos

    def _is_valid(self, x, y):
        if x < 0 or x >= m:
            return False
        if y < 0 or y >= n:
            return False
        if self._box[x][y] != 0:
            return False
        return True
        
    def _next_location(self, pos):
        nexts = []
        for dx, dy in TomatoBox.directions:
            n = (pos[0]+dx, pos[1]+dy, pos[2]+1)
            if not self._is_valid(n[0], n[1]):
                continue

            self._box[n[0]][n[1]] = 1
            nexts.append(n)

        return nexts

    def _is_all_tomato_ripen(self):
        for i in range(self._m):
            for j in range(self._n):
                if self._box[i][j] == 0:
                    return False
        return True

    def get_all_ripe_day(self):
        init_tomatos = self._get_initial_ripen_tomato()

        q = deque(init_tomatos)
        max_time = 0
        while len(q) != 0:
            cur = q.popleft()
            max_time = max(max_time, cur[2])

            nexts = self._next_location(cur)
            q.extend(nexts)
        
        return max_time if self._is_all_tomato_ripen() else -1


if __name__ == '__main__':
    n, m = map(int, stdin.readline().rstrip().split(' '))
    box = []
    for _ in range(m):
        box.append(
            list(map(int, stdin.readline().rstrip().split(' '))))

    tb = TomatoBox(n, m, box)
    print(tb.get_all_ripe_day())
