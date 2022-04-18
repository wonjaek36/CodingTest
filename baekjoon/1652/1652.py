from sys import stdin


class Lying(object):

    def __init__(self, n, mp):
        self._n = n
        self._mp = mp

    def _get_horizontal_place(self):
        place = 0
        for hor in range(self._n):
            ls = [-1]
            ls.extend([i for i in range(self._n) if self._mp[hor][i] == 'X'])
            ls.extend([self._n])
            for a, b in zip(ls[0:], ls[1:]):
                place += 1 if b - a - 1 >= 2 else 0
        return str(place)

    def _get_vertical_place(self):
        place = 0
        for ver in range(self._n):
            ls = [-1]
            ls.extend([i for i in range(self._n) if self._mp[i][ver] == 'X'])
            ls.extend([self._n])
            for a, b in zip(ls[0:], ls[1:]):
                place += 1 if b - a - 1 >= 2 else 0
        return str(place)

    def get_place(self):
        return ' '.join([self._get_horizontal_place(),
                         self._get_vertical_place()])


if __name__ == '__main__':
    mp = []

    n = int(stdin.readline())
    for _ in range(n):
        mp.append(stdin.readline().rstrip())

    ly = Lying(n, mp)
    print(ly.get_place())
