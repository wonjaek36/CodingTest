import heapq
from sys import stdin


class SayMiddle(object):

    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.lcount = 0
        self.hcount = 0
        self.low = []
        self.high = []

    def adjust_tree(self):
        if self.hcount - self.lcount >= 1:
            htop = heapq.heappop(self.high)
            heapq.heappush(self.low, -htop)
            self.hcount -= 1
            self.lcount += 1

        if self.lcount - self.hcount >= 2:
            ltop = -heapq.heappop(self.low)
            heapq.heappush(self.high, ltop)
            self.hcount += 1
            self.lcount -= 1

    def add_num(self, num):
        if self.lcount == 0:
            heapq.heappush(self.low, -num)
            self.lcount += 1
            return

        mid = -self.low[0]
        if num > mid:
            heapq.heappush(self.high, num)
            self.hcount += 1
        else:
            heapq.heappush(self.low, -num)
            self.lcount += 1

        self.adjust_tree()
        
    def get_say_list(self):
        says = []
        for num in self.arr:
            self.add_num(num)
            says.append(-self.low[0])
        return says


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    arr = [int(rd().strip()) for _ in range(n)]

    sm = SayMiddle(n, arr)
    says = sm.get_say_list()
    print('\n'.join(map(str, says)))
