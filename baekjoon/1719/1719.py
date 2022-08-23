from sys import stdin
from functools import reduce


class Parcel(object):

    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        self.edges = edges
        self.dp = [[0x7fffffff]*n for _ in range(n)]
        self.nxt = [[-1]*n for _ in range(n)]

        for i in range(n):
            self.dp[i][i] = 0
            self.nxt[i][i] = 0
        for e in edges:
            self.dp[e[0]-1][e[1]-1] = e[2]
            self.nxt[e[0]-1][e[1]-1] = e[1]
            self.dp[e[1]-1][e[0]-1] = e[2]
            self.nxt[e[1]-1][e[0]-1] = e[0]

    def get_directions(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][j] >\
                            self.dp[i][k] + self.dp[k][j]:
                        self.dp[i][j] = self.dp[i][k]+self.dp[k][j]

                        if i == k:
                            self.nxt[i][j] = j
                        elif self.nxt[i][k] == k:
                            self.nxt[i][j] = k
                        else:
                            self.nxt[i][j] = self.nxt[i][k]
        return self.nxt

if __name__ == '__main__':
    rd = stdin.readline
    n, m = tuple(map(int, rd().split()))
    edges = [tuple(map(int, rd().split())) for _ in range(m)]

    p = Parcel(n, m, edges)
    di_table = p.get_directions()
    di_table_str = list(map(lambda row: list(map(
        lambda x: str(x) if x != 0 else '-', row)), di_table))
    a = reduce(
        lambda a, b: a+' '.join(b)+'\n',
        di_table_str,
        '')
    print(a)
