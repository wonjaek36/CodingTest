import sys
from sys import stdin

import heapq


class Concert(object):

    def __init__(self, n, tickets):
        self._n = n
        self._tickets = tickets
        heapq.heapify(self._tickets)

    def get_best_ticket(self):
        c = 1
        while len(self._tickets) and c == heapq.heappop(self._tickets):
            c += 1

        return c

    
if __name__ == '__main__':
    n = int(stdin.readline().rstrip())
    tickets = list(
        map(int, stdin.readline().rstrip().split(' ')))
    
    cc = Concert(n, tickets)
    print(cc.get_best_ticket())
