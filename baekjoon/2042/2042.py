from sys import stdin


class FenwickTree(object):

    def __init__(self, n):
        self._tree = [0]*(n+1)
        self._arr = [0]*(n+1)
        self._n = n

    def add(self, index, value):
        index += 1
        pos = index 
        diff = value-self._arr[index]

        while pos <= self._n:
            self._tree[pos] += diff
            pos += (pos & -pos)
        self._arr[index] = value

    def sum(self, index):
        index += 1
        pos = index
        
        _sum = 0
        while pos >= 1:
            _sum += self._tree[pos]
            pos &= (pos-1)
        return _sum

    def __str__(self):
        return ' '.join(map(str, self._tree))


if __name__ == '__main__':
    readline = stdin.readline
    n, m, k = map(int, readline().split(' '))
    ft = FenwickTree(n)
    for i in range(n):
        ft.add(i, int(readline()))

    for i in range(m+k):
        a, b, c = list(map(int, readline().split(' ')))

        if a == 1:
            ft.add(b-1, c)
        else:
            print(ft.sum(c-1) - ft.sum(b-2))

