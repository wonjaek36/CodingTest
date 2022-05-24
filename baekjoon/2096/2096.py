from sys import stdin


class Descending(object):

    def __init__(self, n):
        self._n = n

    def step(self, prev, cur, fn, mp):
        cur[0] = fn(prev[0], prev[1]) + mp[0]
        cur[1] = fn(prev[0], prev[1], prev[2]) + mp[1]
        cur[2] = fn(prev[1], prev[2]) + mp[2]
        return cur, [0, 0, 0]

    def descend(self):
        _min_prev, _min_cur = [0, 0, 0], [0, 0, 0]
        _max_prev, _max_cur = [0, 0, 0], [0, 0, 0]

        for i in range(self._n):
            mp = list(map(int, stdin.readline().split(' ')))
            _min_prev, _min_cur = self.step(_min_prev, _min_cur, min, mp)
            _max_prev, _max_cur = self.step(_max_prev, _max_cur, max, mp)
        return max(_max_prev), min(_min_prev)


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    ds = Descending(n)
    max_v, min_v = ds.descend()
    print(max_v, min_v)
