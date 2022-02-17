import sys
from sys import stdin


class MinHeap(object):

    def __init__(self):
        self._heap = [-1]*100002
        self._size = 0

    def hpush(self, v):
        self._size += 1

        pos = self._size
        while pos > 1:
            if self._heap[pos//2] > v:
                self._heap[pos] = self._heap[pos//2]
                pos //= 2
            else:
                break

        self._heap[pos] = v

    def hpop(self):

        if self._size == 0:
            return 0
        
        v = self._heap[1]
        
        pos = 1
        self._size -= 1
        while pos <= self._size:
            left = pos*2
            right = pos*2+1

            if (left <= self._size and right <= self._size):
                if self._heap[left] < self._heap[right] and\
                   self._heap[left] < self._heap[self._size+1]:
                    self._heap[pos] = self._heap[left]
                    pos = left

                elif self._heap[left] >= self._heap[right] and\
                   self._heap[right] < self._heap[self._size+1]:
                    self._heap[pos] = self._heap[right]
                    pos = right

                else:
                    break

            elif left <= self._size:
                if self._heap[left] < self._heap[self._size+1]:
                    self._heap[pos] = self._heap[left]
                    pos = left
                else:
                    break

            else:
                break

        self._heap[pos] = self._heap[self._size+1]
        self._heap[self._size+1] = -1

        return v
    

if __name__ == '__main__':

    h = MinHeap()
    T = int(stdin.readline())
    for i in range(T):
        v = int(stdin.readline())
        if v == 0:
            print(h.hpop())
        else:
            h.hpush(v)
