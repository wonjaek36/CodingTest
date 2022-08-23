from sys import stdin


class Floyd(object):

    def __init__(self, n, m, edges):
        self.n = n
        self.m = m
        self.edges = edges
        self.dp = [
            [0x7fffffff] * n for _ in range(n)]
        for i in range(n):
            self.dp[i][i] = 0
        for edge in edges:
            if self.dp[edge[0]-1][edge[1]-1] > edge[2]:
                self.dp[edge[0]-1][edge[1]-1] = edge[2]

    def get_floyd(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.dp[i][j] > 
                            self.dp[i][k] + self.dp[k][j]):
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j]
        for i in range(self.n):
            for j in range(self.n):
                if self.dp[i][j] == 0x7fffffff:
                    self.dp[i][j] = 0
        return '\n'.join(list(map(lambda x: ' '.join(map(str, x)), self.dp)))

if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    m = int(rd())
    edges = [
        tuple(map(int, rd().split())) for _ in range(m)]

    f = Floyd(n, m, edges)
    print(f.get_floyd())
