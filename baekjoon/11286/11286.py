import sys
from sys import stdin


class AbsMinHeap(object):

    def __init__(self):
        self._heap = [(0, 0)]*100002
        self._size = 0

    def hpush(self, v):
        self._size += 1

        pos = self._size
        v = (abs(v), v)
        while pos > 1:
            if self.less_than(v, self._heap[pos//2]):
                self._heap[pos] = self._heap[pos//2]
                pos //= 2
            else:
                break

        self._heap[pos] = v

    def less_than(self, a, b):
        assert len(a) == 2
        assert len(b) == 2
        return a[0] < b[0] or (a[0] == b[0] and a[1] < b[1])
        
    def hpop(self):

        if self._size == 0:
            return (0, 0)
        
        v = self._heap[1]
        
        pos = 1
        pos_v = self._heap[self._size]
        self._size -= 1
        while pos <= self._size:
            left = pos*2
            right = pos*2+1

            if (left <= self._size and right <= self._size):
                left_v = self._heap[left]
                right_v = self._heap[right]
                if self.less_than(left_v, right_v) and\
                   self.less_than(left_v, pos_v):
                    self._heap[pos] = left_v
                    pos = left

                elif not self.less_than(left_v, right_v) and\
                     self.less_than(right_v, pos_v):
                    self._heap[pos] = right_v
                    pos = right

                else:
                    break

            elif left <= self._size:
                left_v = self._heap[left]
                if self.less_than(left_v, pos_v):
                    self._heap[pos] = self._heap[left]
                    pos = left
                else:
                    break

            else:
                break

        self._heap[pos] = pos_v
        self._heap[self._size+1] = (0, 0)

        return v
    

if __name__ == '__main__':

    h = AbsMinHeap()
    T = int(stdin.readline())
    for i in range(T):
        v = int(stdin.readline())
        if v == 0:
            print(h.hpop()[1])
        else:
            h.hpush(v)

