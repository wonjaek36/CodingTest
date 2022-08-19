from collections import deque
from sys import stdin


class AB(object):

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.visited = set()

    def get_shortest_step(self):
        d = deque([(self.n, 1)])

        while d:
            c, s = d.popleft()
            if c >= 1000000000:
                continue
            if c == self.m:
                return s

            n1 = c * 2
            if n1 not in self.visited:
                self.visited.add(n1)
                d.append((n1, s+1))
            n2 = int(f'{c}1')
            if n2 not in self.visited:
                self.visited.add(n2)
                d.append((n2, s+1))

        return -1


if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    ab = AB(n, m)
    print(ab.get_shortest_step())
