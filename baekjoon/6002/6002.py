from sys import stdin


class JobHunt(object):

    def __init__(self, n, s, edges):
        self.n = n
        self.s = s
        self.edges = edges
        self.inf = 0x7ffffff
        self.visit = [self.inf for _ in range(n+1)]

    def _run_step(self):
        updated = False
        for x, y, v in self.edges:
            if self.visit[y] > self.visit[x]+v:
                self.visit[y] = self.visit[x]+v
                updated = True
        return updated

    def get_profit(self):
        self.visit[self.s] = 0
        for _ in range(self.n-1):
            self._run_step()

        if self._run_step():
            return -1
        return -min(self.visit)


if __name__ == '__main__':
    rd = stdin.readline
    d, p, c, f, s = tuple(map(int, rd().split()))
    # p: path
    # c: cities
    # f: flight path
    # s: Bessie current location
    edges = []
    for _ in range(p):
        a, b = tuple(map(int, rd().split()))
        edges.append((a, b, -d))
    for _ in range(f):
        a, b, v = tuple(map(int, rd().split()))
        edges.append((a, b, v-d))
    jh = JobHunt(c, s, edges)
    x = jh.get_profit()
    if x == -1:
        print(x)
    else:
        print(x+d)
