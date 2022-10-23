from sys import stdin


class MM(object):

    def __init__(self, arr):
        self.arr = sorted(arr)
    
    def all_different(self, a, b, c):
        return a != b and b != c and a != c

    def get_difference(self):
        value = -1 
        for a, b in zip(self.arr[:-1], self.arr[1:-1]):
            value = max(value, abs(self.arr[-1] + a - b * 2))
        for a, b in zip(self.arr[::-1][:-1], self.arr[::-1][1:-1]):
            value = max(value, abs(self.arr[0] + a - b * 2))

        return value


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    arr = [int(rd()) for _ in range(n)]
    mm = MM(arr)
    print(mm.get_difference())
