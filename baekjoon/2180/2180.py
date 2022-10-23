from sys import stdin
from functools import cmp_to_key


class FireStation(object):

    def __init__(self, arr):
        self.arr = arr

    def get_time(self):
        def compares(x, y):
            if x[0] == 0:
                return 1
            if y[0] == 0:
                return -1
            if x[1] == 0 and y[1] == 0:
                return x[0] - y[0]

            return x[1]/x[0] - y[1]/y[0]

        compare_func = cmp_to_key(compares)
        sorted_arr = sorted(self.arr, key=compare_func)

        t = 0
        for a, b in sorted_arr:
            t += (a*t + b)
            t = t % 40000

        return t


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    arr = [tuple(map(int, rd().split())) for i in range(n)]
    
    fs = FireStation(arr)
    print(fs.get_time())

