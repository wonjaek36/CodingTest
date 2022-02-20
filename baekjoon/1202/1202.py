import sys
from sys import stdin
from queue import PriorityQueue


class JewelThief(object):

    def __init__(self, jewels, bags):
        self._bags = bags
        self._jewels = jewels
        self._q = PriorityQueue()

    def steal(self):
        self._bags = sorted(self._bags)
        self._jewels = sorted(self._jewels, key=lambda x: x[0])

        s = 0
        j_p = 0
        num_jewels = len(self._jewels)
        for bag in self._bags:
            for i in range(j_p, num_jewels):
                jewel = self._jewels[i]
                if jewel[0] > bag:
                    i -= 1
                    break
                self._q.put(-jewel[1])
            j_p = i+1
            
            try:
                s -= self._q.get(False)
            except Exception:
                pass

        return s


if __name__ == '__main__':
    n, k = map(int, stdin.readline().split(' '))
    jewels = []
    bags = []

    for i in range(n):
        m, v = map(int, stdin.readline().split(' '))
        jewels.append((m, v))

    for i in range(k):
        c = int(stdin.readline())
        bags.append(c)

    jt = JewelThief(jewels, bags)
    print(jt.steal())
