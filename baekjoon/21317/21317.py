from sys import stdin


class SteppingStone(object):

    def __init__(self, n, jumps, k):
        self.n = n
        self.jumps = jumps
        self.k = k
        self._min_energy = 0x7fffffff 

    def _recursive(self, p, energy, able_big_step):
        if energy >= self._min_energy or p > self.n-1:
            return

        if p == self.n-1:
            self._min_energy = energy
            return

        if able_big_step:
            self._recursive(p+3, energy+self.k, False)
        self._recursive(p+2, energy+self.jumps[p][1], able_big_step)
        self._recursive(p+1, energy+self.jumps[p][0], able_big_step)

    @property
    def min_energy(self):
        if self._min_energy == 0x7fffffff:
            self._recursive(0, 0, True)
        return self._min_energy


if __name__ == '__main__':
    rd = stdin.readline
    jumps = []
    n = int(rd())
    for i in range(n-1):
        jumps.append(tuple(map(int, rd().split(' '))))
    k = int(rd())

    ss = SteppingStone(n, jumps, k)
    print(ss.min_energy)
