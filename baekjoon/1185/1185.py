from sys import stdin


class EuropeTravel(object):

    def __init__(self, n: int, rc: list):
        self.n = n
        self.rc = rc
        self.parents = [i for i in range(n)]

    def _union(self, a, b):
        pa = self._find(a)
        pb = self._find(b)

        self.parents[pa] = pb

    def _find(self, a):
        if self.parents[a] == a:
            return a

        self.parents[a] = self._find(self.parents[a])
        return self.parents[a]

    def get_cost(self):
        rc = sorted(self.rc, key=lambda x: x[2])
        cost = 0
        for a, b, c in rc:
            if self._find(a) == self._find(b):
                continue

            self._union(a, b)
            cost += c

        return cost


if __name__ == '__main__':
    rd = stdin.readline
    n, p = tuple(map(int, rd().split()))
    visit_cost = [int(rd()) for _ in range(n)]
    road_cost = []
    for _ in range(p):
        a, b, c = tuple(map(int, rd().split()))
        a, b = a-1, b-1
        c = visit_cost[a] + visit_cost[b] + c*2

        road_cost.append((a, b, c))

    et = EuropeTravel(n, road_cost)
    print(et.get_cost() + min(visit_cost))

