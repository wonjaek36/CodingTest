from sys import stdin


class FloorDeck(object):

    def __init__(self, n, m, mp):
        self.n = n
        self.m = m
        self.mp = mp
        self._visited = [[False]*m for _ in range(n)]

    def _recursive(self, x, y, d):
        if x < 0 or x >= self.n:
            return
        if y < 0 or y >= self.m:
            return
        if self._visited[x][y]:
            return
        if self.mp[x][y] != d:
            return

        if d == '-':
            self._visited[x][y] = True
            self._recursive(x, y+1, d)
        else:
            self._visited[x][y] = True
            self._recursive(x+1, y, d)


    def get_deck_count(self):
        count = 0
        for i in range(n):
            for j in range(m):
                if not self._visited[i][j]:
                    count += 1
                    self._recursive(i, j, self.mp[i][j])

        return count


if __name__ == '__main__':
    rd = stdin.readline
    n, m = list(map(int, rd().split()))
    mp = [rd().strip() for i in range(n)]

    fd = FloorDeck(n, m, mp)
    print(fd.get_deck_count())
