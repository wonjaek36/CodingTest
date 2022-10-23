from sys import stdin


class Zoo(object):

    def __init__(self, z):
        self._z = z
        self._dp = [[0]*3 for _ in range(self._z+1)]
        self._dp[0][0] = 1

    @property
    def count(self):
        for i in range(1, self._z+1):
            self._dp[i][0] =\
                (self._dp[i-1][0] + self._dp[i-1][1] + self._dp[i-1][2]) % 9901
            self._dp[i][1] =\
                (self._dp[i-1][0] + self._dp[i-1][2]) % 9901
            self._dp[i][2] =\
                (self._dp[i-1][0] + self._dp[i-1][1]) % 9901
        return sum(self._dp[self._z])%9901

if __name__ == '__main__':
    rd = stdin.readline
    z = int(rd())

    z = Zoo(z)
    print(z.count)
