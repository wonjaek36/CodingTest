from sys import stdin


class LongestIncreaseSequence(object):

    def __init__(self, n, arr):
        self.arr = arr
        self.n = n
        self.dp = [1 for _ in range(len(arr))]
        self.trace = [-1 for _  in range(len(arr))]

    def get_longest(self):
        for i in range(self.n):
            for j in range(i):
                if self.arr[i] <= self.arr[j]:
                    continue
                if self.dp[i] < self.dp[j] + 1:
                    self.dp[i] = self.dp[j] + 1
                    self.trace[i] = j

        idx, v = max(enumerate(self.dp), key=lambda x: x[1])
        seq = []
        while idx != -1:
            seq.append(self.arr[idx])
            idx = self.trace[idx]

        return v, seq[::-1]


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    arr = list(map(int, rd().strip().split()))
    lis = LongestIncreaseSequence(n, arr)

    v, seq = lis.get_longest()
    print(v)
    print(' '.join(map(str, seq)))
