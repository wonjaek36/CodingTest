from sys import stdin
from functools import reduce


class ShyomSquare(object):

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self._mp = [[-1]*n for _ in range(n)]
        self._row_cnt = [[0]*d for _ in range(n)]
        self._col_cnt = [[0]*d for _ in range(n)]
        self.flag = False

    def _is_valid_row(self, x, y):
        row_x = map(lambda x: 1 if x == 0 else 0, self._row_cnt[x])
        needs = reduce(lambda x, y: x + y, row_x, 0)
        return (self.n - y - 1) >= needs

    def _is_valid_column(self, x, y):
        col_y = map(lambda y: 1 if y == 0 else 0, self._col_cnt[y])
        needs = reduce(lambda x, y: x + y, col_y, 0)
        return (self.n - x - 1) >= needs

    def _set_val(self, x, y, num):
        self._mp[x][y] = num
        self._row_cnt[x][num] += 1
        self._col_cnt[y][num] += 1

    def _unset_val(self, x, y, num):
        self._mp[x][y] = -1
        self._row_cnt[x][num] -= 1
        self._col_cnt[y][num] -= 1

    def _find_square(self, x, y):
        if x == self.n:
            self.flag = True
            return

        for i in range(d):
            self._set_val(x, y, i)
            if not self._is_valid_column(x, y) or\
               not self._is_valid_row(x, y):
                self._unset_val(x, y, i)
                continue

            self._find_square(x + (y+1) // self.n,
                              (y+1) % self.n)
            if self.flag:
                return
            self._unset_val(x, y, i)

    def get_first_squre(self):
        self._find_square(0, 0)
        return self._mp


if __name__ == '__main__':
    n, d = tuple(map(int, stdin.readline().split()))
    ss = ShyomSquare(n, d)
    _mp = ss.get_first_squre()
    for i in range(n):
        print(' '.join(map(str, _mp[i])))
